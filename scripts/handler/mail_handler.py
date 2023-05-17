import os
import smtplib # simple mail transfer protocol
from pydantic import BaseModel
from email.mime.multipart import MIMEMultipart # support the transfer of single or multiple text
from email.mime.text import MIMEText # standard way of describing data type in a body


class Email(BaseModel):
    rec_email: str
    subject: str
    body: str


def send_email(body, email: Email):
    sender_email = os.environ.get("sender_email")
    sender_password = os.environ.get("sender_password")
    receiver_email = email.rec_email

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = email.subject

    message.attach(MIMEText(str(body), "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)

        server.send_message(message)

        server.quit()

        return {"message": "Email sent successfully"}
    except Exception as e:

        return {"message": str(e)}
