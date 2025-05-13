import sqlite3
from datetime import datetime

def get_db_connection():
    conn = sqlite3.connect('chat_history.db', check_same_thread=False)
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            conversation_id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            conversation_id INTEGER NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            image_data BLOB,
            timestamp TEXT NOT NULL,
            FOREIGN KEY (conversation_id) REFERENCES conversations (conversation_id)
        )
    ''')
    conn.commit()
    conn.close()

def create_new_conversation():
    conn = get_db_connection()
    cursor = conn.cursor()
    timestamp = datetime.now().isoformat()
    cursor.execute('INSERT INTO conversations (created_at) VALUES (?)', (timestamp,))
    conn.commit()
    conversation_id = cursor.lastrowid
    conn.close()
    return conversation_id

def get_conversations():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT conversation_id, created_at FROM conversations ORDER BY created_at DESC')
    conversations = cursor.fetchall()
    conn.close()
    return conversations

def get_messages(conversation_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT role, content, image_data, timestamp FROM messages
        WHERE conversation_id = ?
        ORDER BY timestamp ASC
    ''', (conversation_id,))
    messages = [{"role": role, "content": content, "image_data": image_data, "timestamp": timestamp} 
                for role, content, image_data, timestamp in cursor.fetchall()]
    conn.close()
    return messages

def add_message(conversation_id, role, content, image_data=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    timestamp = datetime.now().isoformat()
    cursor.execute('''
        INSERT INTO messages (conversation_id, role, content, image_data, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (conversation_id, role, content, image_data, timestamp))
    conn.commit()
    conn.close()