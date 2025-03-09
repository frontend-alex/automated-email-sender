def load_email_template():
    with open("templates/email_template.html", "r", encoding="utf-8") as file:
        return file.read()

def generate_email_content(name, custom_message):
    template = load_email_template()
    return template.replace("{name}", name).replace("{custom_message}", custom_message)


# import os
# import subprocess

# def convert_mjml():
#     """Ensures the latest MJML template is converted to HTML before loading."""
#     try:
#         subprocess.run(["mjml", "templates/email_template.mjml", "-o", "templates/email_template.html"], check=True)
#         print("✅ MJML converted successfully!")
#     except Exception as e:
#         print(f"❌ Error converting MJML: {e}")

# def load_email_template():
#     """Loads the HTML email template, ensuring it exists."""
#     template_path = "templates/email_template.html"

#     if not os.path.exists(template_path):
#         print("⚠️ Warning: email_template.html not found! Using fallback message.")
#         return "<p>Hello {name},</p><p>{custom_message}</p>"

#     with open(template_path, "r", encoding="utf-8") as file:
#         return file.read()

# def generate_email_content(name, custom_message):
#     """Generates the email body with personalized content."""
#     convert_mjml()  
#     template = load_email_template()

#     return template.replace("{name}", name).replace("{custom_message}", custom_message)
