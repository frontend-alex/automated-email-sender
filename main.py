import csv
import os
import threading
from core.email_service import send_email

# File paths
CSV_FILE = "data/recipients.csv"
ATTACHMENT_PATH = "data/sample.pdf"  

def process_emails():
    with open(CSV_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        threads = []

        for row in reader:
            email = row["email"].strip()
            name = row["name"].strip()
            custom_message = row["custom_message"].strip()

            thread = threading.Thread(target=send_email, args=(email, name, custom_message, ATTACHMENT_PATH))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

if __name__ == "__main__":
    process_emails()
