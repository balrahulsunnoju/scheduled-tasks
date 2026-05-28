# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import pandas
import datetime as dt
import random
import smtplib
import os

data = pandas.read_csv("birthdays.csv")

email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

today = dt.datetime.now()
today_day = today.day
today_month = today.month

for index, row in data.iterrows():

    if today_day == row["day"] and today_month == row["month"]:

        letter_num = random.randint(1, 3)

        with open(f"letter_templates/letter_{letter_num}.txt") as file:
            f1 = file.read()

        final_letter = f1.replace("[NAME]", row["name"])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)

            connection.sendmail(
                from_addr=email,
                to_addrs=row["email"],
                msg=f"Subject:Birthday Wishes\n\n{final_letter}"
            )
