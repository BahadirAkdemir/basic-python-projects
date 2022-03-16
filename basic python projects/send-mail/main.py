import smtplib
from email.message import EmailMessage
import datetime
import random
import pandas as pd

my_email = ""
my_password = ""

data = pd.read_csv("birthdays.csv")
month = datetime.datetime.now().month
day = datetime.datetime.now().day
birthay_people = data[(data["month"] == month) & (data["day"] == day)]

if len(birthay_people) > 0:

    #with open("quotes.txt", "r") as file:
        #quotes = file.readlines()
        #quote = random.choice(quotes)
        #quote = quote.replace("-", "\n\n~")
    for i in birthay_people.name:
        num = random.choice([1,2,3])
        with open(f"letter_templates/letter_{num}.txt", "r") as file:
            letter = file.read()
            letter = letter.replace("[NAME]", i)
        

        print(letter)

        with smtplib.SMTP('smtp.outlook.com',587, timeout=120) as connection:

            connection.starttls()

            connection.login(my_email, my_password)


            msg = EmailMessage()
            msg.set_content(letter)

            msg['Subject'] = 'Birthday!!!'
            msg['From'] = ""
            msg['To'] = ""

            connection.send_message(msg)
            print("Mail sent")
            connection.close()