import mysql.connector
import bcrypt
from db_config import db_config

def is_username_taken(username):
    """Check if a username already exists in the database."""
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users WHERE username = %s", (username,))
    count = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return count > 0  # Returns True if username exists, False otherwise

def register_user(username, password, email, security_question, security_answer):
    """Registers a new user, preventing duplicate usernames."""
    if is_username_taken(username):
        print("Error: Username already exists.")
        return False

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    hashed_answer = bcrypt.hashpw(security_answer.lower().encode(), bcrypt.gensalt()).decode()

    try:
        cursor.execute("""
            INSERT INTO users (username, password_hash, email, security_question, security_answer_hash)
            VALUES (%s, %s, %s, %s, %s)
        """, (username, hashed_password, email, security_question, hashed_answer))

        conn.commit()
        return True
    except mysql.connector.Error as e:
        print(f"Database Error: {e}")  # Print error for debugging
        return False
    finally:
        cursor.close()
        conn.close()

def login_user(username, password):
    """Authenticates a user by checking credentials."""
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user and bcrypt.checkpw(password.encode(), user['password_hash'].encode()):
        return True
    return False
