# Automated Email Sender

This project allows you to send personalized emails with attachments using Gmail SMTP. It also supports MJML templates for beautifully designed HTML emails.

## 📂 Project Structure
```
📁 email-sender/
│── 📁 core/
│   │── email_service.py       # Handles email generation
│   │── send_email.py          # Sends emails via SMTP
│   │── logger.py              # Logs sent emails
│── 📁 templates/
│   │── email_template.mjml    # MJML template (convert to HTML)
│   │── email_template.html    # Converted HTML email
│── 📁 data/
│   │── recipients.csv         # List of email recipients
│── 📁 logs/                   # Logs email activity (auto-created)
│── .env                       # Stores sensitive email credentials
│── requirements.txt           # Required Python packages
│── README.md                  # Project documentation
│── main.py                    # Entry point to run the script
```

## 🚀 Setup Instructions
### **1️⃣ Install Dependencies**
Activate your virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

Then install Python dependencies:
```bash
pip install -r requirements.txt
```

### **2️⃣ Setup Node.js & MJML**
Since MJML is a Node.js package, install Node.js inside the virtual environment:
```bash
nodeenv -p
npm install -g mjml
```

Verify installation:
```bash
mjml --version
```

### **3️⃣ Configure Environment Variables**
Create a `.env` file in the project root and fill in your email credentials:
```
EMAIL_SENDER="example@gmail.com"
EMAIL_PASSWORD="xx aa mm dd cc"
SMTP_SERVER="smtp.gmail.com"
SMTP_PORT=587
```
🔹 **Use an App Password!** Get one from [Google App Passwords](https://myaccount.google.com/apppasswords).

### **4️⃣ Prepare Recipients List**
Create a `data/recipients.csv` file:
```csv
email,name,custom_message
alexmmech@gmail.com,Alex,Hope you're having a great day!
```

### **5️⃣ Convert MJML to HTML**
Run this command to generate the HTML email:
```bash
mjml templates/email_template.mjml -o templates/email_template.html
```
Alternatively, automate it with Python:
```python
import subprocess

def convert_mjml():
    subprocess.run(["mjml", "templates/email_template.mjml", "-o", "templates/email_template.html"], check=True)
    print("✅ MJML converted successfully!")

convert_mjml()
```

### **6️⃣ Send Emails**
Run the script to send emails:
```bash
python main.py
```

## ✅ Features
✅ Reads **recipients** from CSV  
✅ Sends **personalized** emails  
✅ Supports **attachments**  
✅ Uses **MJML for beautiful templates**  
✅ Logs sent emails in `/logs/`  

