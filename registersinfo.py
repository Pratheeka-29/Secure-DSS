import mysql.connector
import bcrypt
from db_config import db_config

def register_user(username, password, email, security_question, security_answer):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Hash password and security answer
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    hashed_answer = bcrypt.hashpw(security_answer.lower().encode(), bcrypt.gensalt()).decode()

    try:
        # Insert user details into the database
        cursor.execute("""
            INSERT INTO users (username, password_hash, email, security_question, security_answer_hash)
            VALUES (%s, %s, %s, %s, %s)
        """, (username, hashed_password, email, security_question, hashed_answer))

        conn.commit()
        return True  # ✅ Registration successful
    except mysql.connector.Error as e:
        print("Error:", e)
        return False  # ❌ Registration failed
    finally:
        cursor.close()  # ✅ Close cursor
        conn.close()    # ✅ Close connection
