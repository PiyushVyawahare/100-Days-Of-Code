import random
import smtplib
import datetime as dt

MY_EMAIL = "piyushvyawahare2021@gmail.com"
PASSWORD = "Piyush@5807"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 4:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="piyushvyawahare2021@yahoo.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
#
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=2001, month=9, day=25, hour=7, minute=10)
# print(date_of_birth)
