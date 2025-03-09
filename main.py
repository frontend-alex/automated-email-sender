import csv
from core.send_email import send_email

CSV_FILE = "data/recipients.csv"

def send_bulk_emails():
    with open(CSV_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            send_email(row["email"], row["name"], row["custom_message"])

if __name__ == "__main__":
    send_bulk_emails()
