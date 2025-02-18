import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

def send_otp(data):
    
    otp = random.randint(1111,9999)

    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    username = "saivardhan@codegnan.com"
    password = "pktv bszx lnrc bedx"

    from_email = "saivardhan@codegnan.com"
    to_email = data
    subject = "OTP Validation"
    body = f"OTP for Validation is {otp}. \nThank You."

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'plain'))

    server = smtplib.SMTP(smtp_server,smtp_port)
    server.starttls()
    server.login(username,password)
    server.send_message(msg)
    server.quit()

    return otp


