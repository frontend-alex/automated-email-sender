# Automated Email Sender

A Python command-line utility that reads recipients from a CSV, fills an HTML email template, sends messages through SMTP, and records delivery attempts.

## Current status

Small standalone utility. Running main.py sends real emails; it is not a preview or a dry run.

## Features and implementation

- Reads recipient email, name, custom message, and optional attachment paths from CSV.
- Replaces {name} and {custom_message} placeholders in a checked-in HTML template.
- Builds multipart messages, connects with SMTP STARTTLS, and authenticates using environment configuration.
- Logs successful and failed send attempts.

## Technology

Python, the standard csv/email/smtplib libraries, python-dotenv, and an HTML template with an optional MJML authoring source.

## Repository map

| Path | Purpose |
| --- | --- |
| [main.py](<main.py>) | CSV iteration and send orchestration |
| [core/email_service.py](<core/email_service.py>) | HTML template loading and substitution |
| [core/send_email.py](<core/send_email.py>) | SMTP and MIME message construction |
| [core/logger.py](<core/logger.py>) | Send-attempt logging |
| [templates](<templates>) | HTML runtime template and MJML source |
| [requirements.txt](<requirements.txt>) | Python dependencies |

## Local setup

```bash
git clone https://github.com/frontend-alex/automated-email-sender.git
cd automated-email-sender
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, activate .venv with its Scripts activation command instead. Create a local .env with your own SMTP account settings:

```dotenv
EMAIL_SENDER=sender@example.com
EMAIL_PASSWORD=replace-with-your-provider-credential
SMTP_SERVER=smtp.example.com
SMTP_PORT=587
```

Create data/recipients.csv. The header and one illustrative row are:

```csv
email,name,custom_message,attachments
recipient@example.com,Example Person,Your message goes here,
```

The attachments cell accepts comma-separated file paths; quote the CSV cell when it contains multiple paths. Relative paths are resolved from the working directory. Edit templates/email_template.html and the subject in main.py. After reviewing all recipients and content, run python main.py from the repository root to send the batch. The MJML conversion code is commented out, so editing the MJML file alone does not change the runtime HTML.

## Verification

```bash
python -m compileall main.py core
```

This syntax check does not send mail. Inspect a generated body by calling generate_email_content separately and reviewing its output before a deliberate send. No SMTP delivery was attempted during documentation work.

## Limitations and next steps

- No command-line dry-run, retry, deduplication, or resumable batch mechanism is implemented.
- Missing attachment paths are filtered out instead of failing the entire batch.
- Template replacement inserts values directly rather than applying an HTML-escaping template engine.
- Running the script again can resend messages; review logs and recipients before repeating.

## Code review starting points

- [main.py](<main.py>)
- [core/send_email.py](<core/send_email.py>)
- [core/email_service.py](<core/email_service.py>)
