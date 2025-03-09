import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import csv
from core.email_service import generate_email_content

# Load environment variables
load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
ATTACHMENT_PATH = "path/to/your/attachment.pdf"  # Optional

def send_email(to_email, name, custom_message):
    html_content = generate_email_content(name, custom_message)

    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = to_email
    msg["Subject"] = "🚀 Email Sent with My Custom Tool!"

    msg.attach(MIMEText(html_content, "html"))

    if ATTACHMENT_PATH and os.path.exists(ATTACHMENT_PATH):
        with open(ATTACHMENT_PATH, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(ATTACHMENT_PATH)}")
            msg.attach(part)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, to_email, msg.as_string())

        print(f"✅ Email sent to {to_email}")

    except Exception as e:
        print(f"❌ Failed to send email to {to_email}: {e}")

