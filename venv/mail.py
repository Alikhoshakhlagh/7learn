import smtplib
from email.mime.text import MIMEText

sender_email = 'your_email@example.com'
sender_password = 'your_email_password'
receiver_email = 'receiver_email@example.com'

def send_smtp_email(subject, body):
    message = MIMEText(body)

    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = receiver_email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
    except Exception as e:
        print(f"Failed to send email. Error: {e}")