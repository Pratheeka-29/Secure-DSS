 **Secure DSS Application in Python (Streamlit)**.

---

# 🔐 Secure Digital Signature System (DSS) – Mini Project

## Pre-requisites:
1. **Python 3.10+**
2. **Streamlit**
3. **MySQL Server** (running locally)
4. **VS Code** or any code editor

---

## Step 1: Clone or Download the Project

You can either clone this GitHub repo or download the ZIP and extract it:

```bash
git clone https://github.com/Pratheeka-29/Secure-DSS.git
cd Secure-DSS
```

---

## Step 2: Install Required Python Libraries

Make sure to install all required packages:

```bash
pip install streamlit mysql-connector-python cryptography bcrypt
```

> You can also use a `requirements.txt` file for easier setup.

---

## 📁 Project Structure

```
Secure-DSS/
├── app.py                  # Main Streamlit App
├── auth.py                 # Handles registration and login
├── sign_verify.py          # Handles signing and verification
├── generate_hash.py        # Hashing utility
├── db_config.py            # MySQL DB configuration
├── registersinfo.py        # Helper for user information
├── README.md               # This file
└── signatures/             # Stores generated signatures
```

---

## Step 3: Set Up MySQL Database

Make sure your MySQL server is running. Then run the following commands in a MySQL client:

```sql
CREATE DATABASE digital_signature;

USE digital_signature;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    email VARCHAR(255),
    security_question VARCHAR(255),
    security_answer VARCHAR(255)
);
```

You may also need to update `db_config.py` with your MySQL credentials:

```python
config = {
    'user': 'root',
    'password': 'your_password',
    'host': 'localhost',
    'database': 'digital_signature'
}
```

---

## Step 4: Run the App

Start the Streamlit app using:

```bash
streamlit run app.py
```

It will open in your browser at `http://localhost:8501`

---

## 🧠 How It Works

### 1. **User Registration**
- Registers user credentials
- Generates DSA key pair (private/public)
- Stores them securely

### 2. **Login System**
- Verifies bcrypt-hashed password
- Loads keys for signing/verifying messages

### 3. **Message Signing**
- Input any message → hashes it → signs with private key
- Signature is displayed for sharing/verification

### 4. **Message Verification**
- Input message + signature + username → verifies using public key
- Confirms if signature is valid or tampered

---

## Expected Results

- ✅ Successfully signing a message generates a valid signature.
- ❌ Changing the message or signature will cause the verification to **fail**.
- ⚠️ If username doesn’t exist, the system shows an error.

---

## 🔒 Security Features

- Bcrypt password hashing
- Public/private key pairs stored securely
- Digital signatures are message-specific
- Verification checks ensure message integrity

---

🔒 Features
User-friendly Streamlit interface

Secure password hashing using bcrypt

DSA key generation and message signing

Message verification using public keys

Signature tampering detection

Error handling and alerts

alerts

🧪 Test Cases
Case	Expected Output
Valid signature & correct user	✅ Signature is valid
Tampered message or signature	❌ Signature is NOT valid
Wrong username	❌ Error loading public key
Missing inputs	⚠️ Prompt to fill all fields

📌 Notes
All signed messages are stored locally.

Keys are unique per user and regenerated on registration.

Streamlit makes the app interactive and easy to use.


## Conclusion

Successfully developed a **Secure Digital Signature System** using Python and Streamlit with cryptographic features. This system enables signing and verifying messages using public-key cryptography ensuring **data integrity**, **authenticity**, and **non-repudiation**.

---



