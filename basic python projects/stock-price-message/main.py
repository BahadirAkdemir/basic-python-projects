STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY=""
NEWS_API_KEY=""
my_email = ""
my_password = ""

import requests
import datetime
from newsapi import NewsApiClient
import smtplib
from email.message import EmailMessage

today = datetime.datetime.now()
day=today.day
month=today.month
weekday=today.weekday()


def send_msg(title,content,msg_to):
    with smtplib.SMTP('smtp.outlook.com',587, timeout=120) as connection:

            connection.starttls()

            global my_email
            global my_password

            connection.login(my_email, my_password)


            msg = EmailMessage()
            msg.set_content(content)

            msg['Subject'] = title
            msg['From'] = my_email
            msg['To'] = msg_to

            connection.send_message(msg)
            print("Mail sent")
            connection.close()


if weekday < 5:
    print("Today is a weekday")
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={STOCK_API_KEY}"
    r = requests.get(url)
    data = r.json()
    day=datetime.datetime.today() - datetime.timedelta(days=1)
    previous_day=day-datetime.timedelta(days=1)
    date_today=str(day.strftime("%Y-%m-%d"))
    date_previous_day=str(previous_day.strftime("%Y-%m-%d"))
    today_close=float(data["Time Series (Daily)"][date_today]["4. close"])
    yesterday_close=float(data["Time Series (Daily)"][date_previous_day]["4. close"])
    ratio=float(today_close/yesterday_close)
    if 0.9>=ratio or ratio >= 1.1:
        print("Dramatically different,check the news")
        newsapi2 = NewsApiClient(api_key=NEWS_API_KEY)

        all_articles = newsapi2.get_everything(q=COMPANY_NAME,
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk',
                                      from_param='2022-02-20',
                                      to='2022-03-20',
                                      language='en',
                                      sort_by='relevancy',
                                      page=1)
        msg=""
        if ratio >= 1.1:
            msg_title=f"{STOCK} stock goes up!"
        else:
            msg_title=f"{STOCK} stock goes down!"
        msg_content=f"Here is the related news:\n\n{all_articles['articles'][0]['title']}"
        send_msg(msg_title,msg_content,"")     
else:
    print("Today is a weekend")
    pass

