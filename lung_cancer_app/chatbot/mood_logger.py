import sqlite3
from datetime import datetime

# Connect to the database
conn = sqlite3.connect("mood_logs.db", check_same_thread=False)
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS mood_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        mood TEXT,
        timestamp TEXT
    )
""")
conn.commit()

# Function to log mood
def log_mood_to_db(name, mood):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO mood_logs (name, mood, timestamp) VALUES (?, ?, ?)", (name, mood, timestamp))
    conn.commit()
