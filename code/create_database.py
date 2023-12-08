import sqlite3

# Connect to SQLite database (creates a new file if not exists)
conn = sqlite3.connect('chatbot_database.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store chatbot data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS chat_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        message TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
