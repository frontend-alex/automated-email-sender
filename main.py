import csv
import os
from core.send_email import send_email

CSV_FILE = "data/recipients.csv"

def send_bulk_emails():
    """Reads recipients from CSV and sends personalized emails with multiple attachments."""
    with open(CSV_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            file_paths = []
            if "attachments" in row and row["attachments"].strip():
                raw_attachments = row["attachments"].strip()

                file_paths = [path.strip() for path in raw_attachments.split(",")]

                file_paths = [path for path in file_paths if os.path.exists(path)]

            send_email(row["email"], row["name"], row["custom_message"], file_paths if file_paths else None)

if __name__ == "__main__":
    send_bulk_emails()
