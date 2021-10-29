import random
import pandas as pd
import smtplib
import datetime as dt

MY_EMAIL = "piyushvyawahare2021@gmail.com"
PASSWORD = "Piyush@5807"

now = dt.datetime.now()
month = now.month
day = now.day

birthdays = pd.read_csv("birthdays.csv")
birthdays_dictionary = birthdays.to_dict(orient="records")

for dictionary in birthdays_dictionary:
    if dictionary['month'] == month and dictionary['day'] == day:
        num = random.randint(1, 3)
        with open(f"letter_templates/letter_{num}.txt") as file:
            content = file.read()
            content = content.replace("[NAME]", dictionary["name"])

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=dictionary["email"],
                msg=f"Subject:Happy Birthday!\n\n{content}"
            )
