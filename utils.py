import sqlite3
from datetime import datetime

DB_NAME = 'bot_data.db'

def setup_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS broadcasts
        (content_type TEXT, sender_id INTEGER, timestamp TEXT)
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS groups
        (group_id INTEGER PRIMARY KEY, group_name TEXT, joined_at TEXT)
    ''')
    conn.commit()
    conn.close()

def get_db():
    return sqlite3.connect(DB_NAME)

def get_all_group_ids():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT group_id FROM groups")
    group_ids = [row[0] for row in cursor.fetchall()]
    conn.close()
    return group_ids

def add_group(group_id, group_name):
    conn = get_db()
    cursor = conn.cursor()
    joined_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT OR REPLACE INTO groups VALUES (?, ?, ?)", (group_id, group_name, joined_at))
    conn.commit()
    conn.close()

def get_group_count():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM groups")
    count = cursor.fetchone()[0]
    conn.close()
    return count

def save_broadcast(content_type, sender_id, timestamp):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO broadcasts VALUES (?, ?, ?)", (content_type, sender_id, timestamp))
    conn.commit()
    conn.close()