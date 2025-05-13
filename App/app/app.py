import streamlit as st
from dotenv import load_dotenv
import os
from PIL import Image
import io
import base64
from datetime import datetime
from database import init_db, create_new_conversation, get_conversations, get_messages, add_message
from api_caller import generate_response 

# Load environment variables
load_dotenv()

# Initialize database
init_db()

# Custom CSS
st.markdown("""
    <style>
    .chat-history {
        margin-bottom: 100px; /* Adjust based on chat input height */
    }
    </style>
""", unsafe_allow_html=True)

# Page title
st.title('🖼️ Visual Question Answering')

# Sidebar for conversation list and new conversation button
with st.sidebar:
    st.header("Conversations")
    if st.button("New Conversation"):
        new_conversation_id = create_new_conversation()
        st.session_state['current_conversation_id'] = new_conversation_id
        st.session_state['messages'] = []  # Clear current messages

    # Get and display all conversations
    conversations = get_conversations()
    if conversations:
        for conv_id, created_at in conversations:
            if st.button(f"Conversation {conv_id} ({created_at[:19]})", key=f"conv_{conv_id}"):
                st.session_state['current_conversation_id'] = conv_id
                st.session_state['messages'] = get_messages(conv_id)
    else:
        st.write("No conversations yet.")

# Main chat area
if 'current_conversation_id' not in st.session_state:
    st.write("Please start a new conversation or select an existing one.")
else:
    current_conversation_id = st.session_state['current_conversation_id']
    messages = st.session_state['messages']

    # Display chat history for the current conversation
    st.markdown('<div class="chat-history">', unsafe_allow_html=True)
    for message in messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'])
            if message['image_data']:
                image = Image.open(io.BytesIO(message['image_data']))
                st.image(image, caption="Uploaded Image")
    st.markdown('</div>', unsafe_allow_html=True)

    # Chat input with file upload
    if input_data := st.chat_input(
        "Ask a question and upload an image",
        accept_file=True,
        file_type=["jpg", "jpeg", "png"],
        key="chat_input"
    ):
        prompt = input_data.get("text", "")
        uploaded_file = input_data.get("files", None)
        image_data = None

        # Enforce constraint: both prompt and image must be provided
        if not prompt or not uploaded_file:
            st.error("Please provide both a question and an image.")
        else:
            try:
                # Read the uploaded file's raw bytes
                image_data = uploaded_file[0].read()  # Get bytes directly from the uploaded file
                # Verify it's a valid image
                Image.open(io.BytesIO(image_data))
            except Exception as e:
                st.error(f"Invalid image file: {str(e)}")
                st.stop()

            # Display the uploaded image and text
            with st.chat_message('user'):
                image = Image.open(io.BytesIO(image_data))
                st.image(image, caption="Uploaded Image")
                st.markdown(prompt)

            # Add user message to the database with image data
            add_message(current_conversation_id, "user", prompt, image_data)
            # Append user's message to session state
            st.session_state['messages'].append({
                "role": "user",
                "content": prompt,
                "image_data": image_data,
                "timestamp": datetime.now().isoformat()
            })

            # Prepare conversation for Gemini API with only the current user message
            image_b64 = base64.b64encode(image_data).decode('utf-8')
            conversation = [
                {
                    "role": "user",
                    "parts": [
                        {"text": prompt},
                        {
                            "inline_data": {
                                "mime_type": "image/png",  # Note: Could be made dynamic based on file type
                                "data": image_b64
                            }
                        }
                    ]
                }
            ]

            # Get response from Gemini model
            with st.chat_message('assistant'):
                # client = st.session_state['model']
                try:
                    answer = generate_response(conversation)
                    if answer:
                        st.markdown(answer)
                        # Add assistant's message to the database
                        add_message(current_conversation_id, "assistant", answer)
                        # Append assistant's message to session state
                        st.session_state['messages'].append({
                            "role": "assistant",
                            "content": answer,
                            "image_data": None,
                            "timestamp": datetime.now().isoformat()
                        })
                    else:
                        st.error("No valid response received from the Gemini model.")
                except RuntimeError as e:
                    st.error(str(e))