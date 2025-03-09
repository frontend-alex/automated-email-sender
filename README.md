# 📧 Advanced Python Email Sender

## 📌 Overview
This is a **scalable and customizable email sender** built with Python. It allows you to send **personalized emails with attachments** to multiple recipients listed in a CSV file. It also logs sent emails for tracking purposes.

---

## 🚀 Features
✅ Reads recipients from a CSV file  
✅ Sends **personalized** emails with names & custom messages  
✅ Supports **attachments** (optional)  
✅ Uses **multi-threading** for fast email sending  
✅ **Logs all sent emails** in `logs/sent_emails.log`  
✅ Uses a **.env file for security** (Gmail App Password)  
✅ **Scalable & Modular Codebase** for easy improvements  

---

## 📂 Project Structure
```
📁 email-sender/
│── 📁 core/
│   │── email_service.py
│   │── logger.py
│── 📁 templates/
│   │── email_template.html
│── 📁 logs/  (auto-created)
│── 📁 data/
│   │── recipients.csv  (Create this manually)
│── .env  (Create this manually)
│── main.py
│── requirements.txt
│── README.md
```

---

## 📋 Setup Instructions
### **1️⃣ Install Dependencies**
Ensure you have Python installed. Then, install required libraries:
```bash
pip install -r requirements.txt
```

### **2️⃣ Create a `.env` File**
You need to create a `.env` file in the root directory and fill in the required credentials:
```ini
EMAIL_SENDER="your-email@gmail.com"
EMAIL_PASSWORD="your-app-password"  # Use an App Password, not your real password
SMTP_SERVER="smtp.gmail.com"
SMTP_PORT=587
```
🔹 **Important:** Enable **2-Step Verification** on your Google account and generate an **App Password** from [Google App Passwords](https://myaccount.google.com/apppasswords).

### **3️⃣ Create a `data/` Folder & `recipients.csv` File**
Inside the `data/` folder, create a `recipients.csv` file containing recipient details:
```csv
email,name,custom_message
alexmmech@gmail.com,Alex,Hey Alex, this is a test email just for you!
info@wearebrain.com,WeAreBrain Team,I'm excited about your work on AI projects.
```

### **4️⃣ Run the Script**
Once everything is set up, run the script:
```bash
python main.py
```

### **5️⃣ Check Logs**
To see which emails were sent successfully:
```bash
type logs/sent_emails.log  # Windows
cat logs/sent_emails.log  # macOS/Linux
```

---

## 📌 Customization
### **Modify the Email Template**
Edit `templates/email_template.html` to change the email design.

### **Add Attachments**
Modify `main.py` to specify a file in the `ATTACHMENT_PATH` variable.

### **Improve Scalability**
- Use **Gmail API** instead of SMTP for better performance.
- Integrate with **Flask/Django** to build a web interface.
- Add **Celery** for scheduled email sending.


