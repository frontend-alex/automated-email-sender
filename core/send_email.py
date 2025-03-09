import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from dotenv import load_dotenv
from core.logger import log_email
from core.email_service import generate_email_content  

load_dotenv()
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))

def send_email(to_email, name, custom_message, file_paths=None):
    """Sends an email with multiple attachments."""
    try:
        email_body = generate_email_content(name, custom_message)

        msg = MIMEMultipart()
        msg["From"] = EMAIL_SENDER
        msg["To"] = to_email
        msg["Subject"] = "Personalized Email from My Custom Tool"
        msg.attach(MIMEText(email_body, "html"))  

        if file_paths:
            for file_path in file_paths:
                file_path = file_path.strip()
                if file_path and os.path.exists(file_path):
                    with open(file_path, "rb") as f:
                        attachment = MIMEApplication(f.read(), _subtype=os.path.splitext(file_path)[1][1:])
                        attachment.add_header("Content-Disposition", f"attachment; filename={os.path.basename(file_path)}")
                        msg.attach(attachment)

        # Send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, to_email, msg.as_string())

        log_email(to_email, f"Sent Successfully ✅ Attachments: {file_paths if file_paths else 'None'}")
        print(f"✅ Email sent to {to_email} with attachments: {file_paths if file_paths else 'None'}")

    except Exception as e:
        log_email(to_email, f"Failed: {str(e)} ❌")
        print(f"❌ Failed to send email to {to_email}: {str(e)}")
