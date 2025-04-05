import bcrypt

security_answer = "i am lisa"  # Replace with the actual answer
hashed_answer = bcrypt.hashpw(security_answer.lower().encode(), bcrypt.gensalt()).decode()

print(hashed_answer)  # Copy this output for the next step
