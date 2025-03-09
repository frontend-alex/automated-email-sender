import datetime
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "sent_emails.log")

os.makedirs(LOG_DIR, exist_ok=True)

def log_email(email, status):
    log_entry = f"{datetime.datetime.now()} - {email} - {status}"
    
    with open(LOG_FILE, "a") as log:
        log.write(log_entry + "\n")
    print(log_entry) 
