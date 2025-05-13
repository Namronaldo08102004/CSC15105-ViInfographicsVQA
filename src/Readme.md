# Visual Question Answering App

This is a Streamlit-based web application for Visual Question Answering (VQA). Users can upload images, ask questions about them, and receive answers powered by the Gemini API. The app stores conversation history in a SQLite database, allowing users to revisit past interactions. The API service is implemented using FastAPI and run via a Jupyter Notebook.

## Prerequisites

- **Python 3.8+**: Ensure Python is installed on your system.
- **Virtual Environment**: Recommended for managing dependencies.
- **Gemini API Key**: Obtain your key from [Google AI Studio](https://aistudio.google.com/app/apikey).
- **Ngrok**: Required for exposing the API service locally (optional for development).
- **Jupyter Notebook**: Needed to run the API service.

## Project Structure

```
project_root/
├── api_service/
│   ├── .env.example
│   └── fastapi-full.ipynb
├── app/
│   ├── .env.example
│   ├── api_caller.py
│   ├── app.py
│   └── database.py
├── requirements.txt
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

1. Copy the `.env.example` file from the `app` directory to create a `.env` file:

   ```bash
   cp app/.env.example app/.env
   ```

2. Edit the `.env` file to include your **Gemini API Key** and **Ngrok URL** (obtained from running the API service):

   ```env
   API_URL=<your-ngrok-url>
   GEMINI_API_KEY=<your-gemini-api-key>
   ```

   **Note**: If the `api_service` directory uses a separate `.env.example`, you may need to copy and configure it similarly (e.g., `cp api_service/.env.example api_service/.env`) based on its requirements.

### 5. Run the API Service (Jupyter Notebook)

1. Ensure the Jupyter Notebook kernel is set to the virtual environment.
2. Navigate to the `api_service` directory:

   ```bash
   cd api_service
   ```

3. Open `fastapi-full.ipynb` and select **Run All** to start the API service.
4. Copy the **Ngrok URL** provided by the notebook and update the `API_URL` in the `app/.env` file.

### 6. Run the Streamlit App

1. Navigate to the `app` directory:

   ```bash
   cd app
   ```

2. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

3. Open the provided URL (e.g., `http://localhost:8501`) in your browser to access the app.

## Usage

- **Start a New Conversation**: Click "New Conversation" in the sidebar to begin.
- **Upload Image and Ask Questions**: Use the chat input to upload an image (JPG, JPEG, or PNG) and type a question.
- **View History**: Select a conversation from the sidebar to view past messages and images.
- **Requirements**: Both an image and a question are required for each query.

## Troubleshooting

- **Invalid Image File**: Ensure uploaded images are valid (JPG, JPEG, or PNG).
- **API Errors**: Verify the Gemini API key and Ngrok URL in the `app/.env` file.
- **Dependency Issues**: Confirm all packages are installed in the virtual environment.

## Dependencies

Listed in `requirements.txt`:

- `requests`: For API calls.
- `python-dotenv`: For environment variable management.
- `streamlit`: For the web interface.
- `pillow`: For image processing.

## Contributing

Feel free to submit issues or pull requests to improve the project. Ensure changes are tested in a virtual environment.
