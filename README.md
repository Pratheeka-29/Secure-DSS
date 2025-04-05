
```markdown
# 🔐 Secure DSS Application in Python (Streamlit)

---

## 📌 Pre-requisites

- Python 3.10+
- Streamlit
- MySQL Server (running locally)
- Code editor (e.g., VS Code)

---

## 📥 Step 1: Clone or Download the Project

You can either clone this GitHub repository or download the ZIP and extract it:

```bash
git clone https://github.com/Pratheeka-29/Secure-DSS.git
cd Secure-DSS
```

---

## ⚙️ Step 2: Install Required Python Libraries

Install all required Python libraries using:

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

## 🛠️ Step 3: Set Up MySQL Database

Ensure your MySQL server is running. Use a MySQL client (e.g., MySQL Workbench or CLI) and run:

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

### 🔧 Configure MySQL Credentials

Update the `db_config.py` file with your MySQL credentials:

```python
config = {
    'user': 'root',
    'password': 'your_password',
    'host': 'localhost',
    'database': 'digital_signature'
}
```

---

## ▶️ Step 4: Run the App

Start the Streamlit application:

```bash
streamlit run app.py
```

Open your browser and navigate to `http://localhost:8501`

---

## 🧠 How It Works

### 1. 📝 User Registration
- User provides details (username, email, password, security question/answer).
- DSA key pair (private & public) is generated.
- Keys are securely stored.

### 2. 🔐 Login System
- Passwords are verified using `bcrypt`.
- User credentials and keys are loaded securely.

### 3. ✍️ Message Signing
- User inputs a message.
- Message is hashed and digitally signed using private key.
- A unique signature is generated.

### 4. ✅ Signature Verification
- User provides the message, signature, and username.
- System verifies authenticity using stored public key.
- Detects tampering or mismatches.

---

## ✅ Expected Results

- ✅ Signing a message successfully generates a valid signature.
- ❌ Modifying the message or signature will make the verification fail.
- ⚠️ Incorrect username triggers a public key error.

---

## 🔐 Security Features

- Secure login using **bcrypt password hashing**
- **DSA key pairs** for each user
- Signature verification ensures **message integrity**
- Digital signatures are **message-specific**
- Tampering or key mismatches are detected automatically

---

## 🌟 Key Features

- ✅ User-friendly Streamlit web interface
- 🔐 Secure user registration and login
- 🔑 Key-based digital message signing
- 🧾 Message integrity verification using public keys
- 🚨 Tampering and error detection
- 🔁 Instant feedback and alerts for users

---

## 🧪 Test Cases

| Test Case                          | Expected Output              |
|-----------------------------------|------------------------------|
| Valid signature & correct user    | ✅ Signature is valid         |
| Tampered message or signature     | ❌ Signature is NOT valid     |
| Wrong username                    | ❌ Error loading public key   |
| Missing inputs                    | ⚠️ Prompt to fill all fields  |

---

## 🗒️ Notes

- All signed messages are saved locally in the `signatures/` folder.
- Each user gets a unique key pair upon registration.
- Streamlit provides a real-time, interactive experience.
- Ensure MySQL server is running before using the app.

---

## 🏁 Conclusion

Successfully developed a **Secure Digital Signature System** using Python and Streamlit with cryptographic DSA features. This system enables signing and verifying messages using public-key cryptography, ensuring:

- 🔒 Data Integrity  
- ✅ Authenticity  
- 🚫 Non-repudiation  

---

