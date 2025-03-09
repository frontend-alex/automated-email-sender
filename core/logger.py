import os
from datetime import datetime

LOG_FILE = "logs/sent_emails.log"

def log_email(recipient, status):
    """Logs email activity with timestamps."""
    os.makedirs("logs", exist_ok=True) 

    with open(LOG_FILE, "a", encoding="utf-8") as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] To: {recipient} - Status: {status}\n")

    print(f"📜 Logged: {recipient} - {status}")
