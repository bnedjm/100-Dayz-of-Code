import os
import string
from email.mime.text import MIMEText
from twilio.rest import Client
from smtplib import *

# Twilio Account Information
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
MY_NUMBER = os.environ.get("MY_NUMBER")

# Google Mail Account Information
EMAIL_SENDER = os.environ.get("EMAIL_SENDER")
APP_PASSWORD = os.environ.get("APP_PASSWORD")

class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message):
        # Twilio send message
        notification = self.client.messages.create(
            body=message,
            from_="+15108801602",
            to=MY_NUMBER,
        )
        # print message status
        print(notification.status)

    def send_emails(self, body: string, emails: list):
        # format the email
        text_type = "html"
        msg = MIMEText(body.replace("\n", "<br>"), text_type, 'utf-8')
        msg['Subject'] = "New Low Price Flight!"
        # SMTP send email
        with SMTP("smtp.gmail.com", port=587) as connect:
            connect.starttls()
            connect.login(user=EMAIL_SENDER, password=APP_PASSWORD)
            connect.sendmail(
                from_addr=EMAIL_SENDER,
                to_addrs=emails,
                msg=msg.as_string(),
            )
