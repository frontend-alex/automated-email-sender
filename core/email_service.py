import smtplib
import os
import mimetypes
from email.message import EmailMessage
from dotenv import load_dotenv
from core.logger import log_email

# Load credentials from .env
load_dotenv()
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))

TEMPLATE_PATH = "templates/email_template.html"
with open(TEMPLATE_PATH, "r", encoding="utf-8") as file:
    HTML_TEMPLATE = file.read()

def send_email(to_email, name, custom_message, attachment_path=None):
    try:
        html_body = HTML_TEMPLATE.format(name=name, custom_message=custom_message)

        msg = EmailMessage()
        msg["From"] = EMAIL_SENDER
        msg["To"] = to_email
        msg["Subject"] = f"Hello {name}, A Special Message for You!"
        msg.set_content("This email requires an HTML viewer.")
        msg.add_alternative(html_body, subtype="html")

        if attachment_path and os.path.exists(attachment_path):
            mime_type, _ = mimetypes.guess_type(attachment_path)
            main_type, sub_type = mime_type.split("/") if mime_type else ("application", "octet-stream")
            
            with open(attachment_path, "rb") as file:
                msg.add_attachment(file.read(), maintype=main_type, subtype=sub_type, filename=os.path.basename(attachment_path))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        
        log_email(to_email, "Success")
        print(f"✅ Email sent to {to_email}")

    except Exception as e:
        log_email(to_email, f"Failed: {str(e)}")
        print(f"❌ Failed to send email to {to_email}: {e}")
