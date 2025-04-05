from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
import mysql.connector
from db_config import db_config
import base64

def generate_and_store_keys(user_name):
    """Generate DSA key pair and store it in the database"""
    key = DSA.generate(2048)
    public_key = key.publickey().export_key().decode()
    private_key = key.export_key().decode()

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO dss_keys (user_name, public_key, private_key)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE public_key=%s, private_key=%s
    """, (user_name, public_key, private_key, public_key, private_key))

    conn.commit()
    cursor.close()
    conn.close()

    return public_key, private_key

def sign_message(user_name, message):
    """Sign a message using the user's private key"""
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT private_key FROM dss_keys WHERE user_name = %s", (user_name,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if not row:
        print(f"Error: No private key found for {user_name}")
        return None

    private_key = DSA.import_key(row['private_key'])
    hash_obj = SHA256.new(message.encode())
    signer = DSS.new(private_key, 'fips-186-3')
    signature = signer.sign(hash_obj)
    
    return base64.b64encode(signature).decode()

def load_public_key(username):
    """Retrieve the public key from the database"""
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT public_key FROM dss_keys WHERE user_name = %s", (username,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if not row:
        print(f"Error: No public key found for {username}")
        return None

    return DSA.import_key(row['public_key'])

def verify_signature(username, message, signature):
    """Verify the signature of a given message"""
    public_key = load_public_key(username)
    if not public_key:
        print(f"Verification failed: No public key for {username}")
        return False

    try:
        hash_obj = SHA256.new(message.encode())
        signature_bytes = base64.b64decode(signature)
        verifier = DSS.new(public_key, 'fips-186-3')
        verifier.verify(hash_obj, signature_bytes)
        print("Signature is VALID ✅")
        return True
    except ValueError:
        print("Signature verification failed ❌: Signature mismatch")
        return False
    except Exception as e:
        print(f"Error during verification: {e}")
        return False
