import time
import json
import secrets
import os

# Initialize database file if it doesn't exist
DB_FILE = "verification_db.json"
if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump({}, f)

def generate_secure_code():
    """Generates a cryptographically secure 4-digit verification code."""
    return str(secrets.randbelow(9000) + 1000)

def save_code_to_db(username, code):
    """Securely maps and saves the username and token to our local JSON database."""
    try:
        with open(DB_FILE, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        data = {}
        
    data[username.lower()] = {
        "code": code,
        "timestamp": time.time(),
        "verified": False
    }
    
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)
    print(f"[SECURITY INFO] Cached code {code} for user: {username}")

def main_bot_loop():
    print("[SYSTEM START] ModBot Server Core is online and listening...")
    
    while True:
        # ====================================================================
        # PLACE YOUR YAPPER CLIENT API LISTENER/STREAM CODE HERE
        # Example: 
        # message = yapper_client.receive_dm()
        # ====================================================================
        
        # Simulated wrapper for testing your terminal logic:
        # if message.content == "!apply":
        #     user = message.author
        #     code = generate_secure_code()
        #     save_code_to_db(user, code)
        #     yapper_client.send_dm(user, f"Your verification code is {code}")
        
        # Keeps the cloud CPU execution tracking steady and prevents overheating
        time.sleep(1)

if __name__ == "__main__":
    main_bot_loop()
