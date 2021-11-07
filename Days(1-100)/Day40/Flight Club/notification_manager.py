import smtplib
from twilio.rest import Client

TWILIO_SID = "AC77e9d87ccf45ef690cdf729ac3a6d1d0"
TWILIO_AUTH_TOKEN = "e87d9c7bf1f3576ab4f70ce2ac1a3c6d"
TWILIO_VIRTUAL_NUMBER = "+19863004435"
TWILIO_VERIFIED_NUMBER = "+919309982738"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "piyushvyawahare2021@gmail.com"
MY_PASSWORD = "Piyush@5807"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
