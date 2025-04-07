import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(message):
    email = 'adamidrissi177@gmail.com'
    password = "PASSWORD2" 
    receiver = 'adamidrissi@gmail.com'
    host = 'smtp.gmail.com'
    port = 465

    # Create the email message
    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = receiver
    msg["Subject"] = "Your Article"

    # Attach the message (content) as MIMEText, set to UTF-8 encoding
    msg.attach(MIMEText(message, "plain", "utf-8"))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(email, password)
        # Send the email as a string with UTF-8 encoding
        server.sendmail(email, receiver, msg.as_string())

    print("Email sent successfully")
