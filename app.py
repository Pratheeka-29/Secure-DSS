import streamlit as st
from sign_verify import generate_and_store_keys, sign_message, verify_signature
from auth import register_user, login_user, is_username_taken

def main():
    st.title("Secure DSS Application")
    menu = ["Home", "Login", "Register", "Sign & Verify Message"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Welcome to Secure DSS App")
    
    elif choice == "Register":
        st.subheader("Create an Account")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        email = st.text_input("Email")
        security_question = st.text_input("Security Question")
        security_answer = st.text_input("Security Answer")
        
        if st.button("Register"):
            if is_username_taken(username):  # Check if the username exists
                st.error("Username already exists! Please choose a different one.")
            else:
                success = register_user(username, password, email, security_question, security_answer)
                if success:
                    generate_and_store_keys(username)
                    st.success("Account created successfully! You can now log in.")
                else:
                    st.error("Registration failed due to an error!")

    elif choice == "Login":
        st.subheader("Login to Your Account")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            if login_user(username, password):
                st.success(f"Welcome {username}!")
            else:
                st.error("Invalid username or password")

    elif choice == "Sign & Verify Message":
        st.subheader("Sign and Verify Messages")
        username = st.text_input("Enter your username")
        message = st.text_area("Enter the message to sign")
        
        if st.button("Sign Message"):
            if username and message:
                signature = sign_message(username, message)
                if signature:
                    st.text_area("Generated Signature", signature, height=100)
                else:
                    st.error("Error generating signature. Ensure username is correct and registered.")
            else:
                st.error("Please enter both username and message.")
        
        st.subheader("Verify a Signed Message")
        verify_message = st.text_area("Enter the message to verify")
        signature_to_verify = st.text_area("Enter the signature")
        verify_user = st.text_input("Enter the username for verification")
        
        if st.button("Verify Signature"):
            if verify_message and signature_to_verify and verify_user:
                is_valid = verify_signature(verify_user, verify_message, signature_to_verify)
                if is_valid:
                    st.success("Signature is valid!")
                else:
                    st.error("Signature is NOT valid!")
                    st.warning("Possible reasons:\n"
                               "- Wrong username\n"
                               "- Message tampered\n"
                               "- Signature corrupted")
            else:
                st.error("Please provide all required inputs for verification.")

if __name__ == "__main__":
    main()
