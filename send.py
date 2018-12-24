import forecastio
import smtplib
import requests
from configs import *

lat = "47.57070050000001"
lng =  "-122.38715259999998"

url = 'https://quotes.rest/qod'
res = requests.get(url)
resData = res.json()
data = resData['contents']['quotes']
#data = [{u'category': u'inspire', u'permalink': u'https://theysaidso.com/quote/74RZL1_lOJ5uScr4h8ntCgeF/napoleon-hill-effort-only-fully-releases-its-reward-after-a-person-refuses-to-qu', u'tags': [u'effort', u'inspire'], u'quote': u'Effort only fully releases its reward after a person refuses to quit.', u'author': u'Napoleon Hill', u'length': u'69', u'background': u'https://theysaidso.com/img/bgs/man_on_the_mountain.jpg', u'date': u'2018-12-23', u'title': u'Inspiring Quote of the day', u'id': u'74RZL1_lOJ5uScr4h8ntCgeF'}]

quote = data[0]["quote"]
author = data[0]["author"]

forecast = forecastio.load_forecast(api_key, lat, lng)

current = forecast.currently()
hourly =  forecast.hourly()

user = "starbuckswork01@gmail.com"
recipient = "grayson.stream@gmail.com"

s = hourly.summary
summary = s.encode('ascii', errors='ignore').decode()

body = """\
Subject: Daily Weather Email \n
Summary for the day: {3} \n
Currently the weather is: {0} degress \n
It Feels like: {1} degress\n
The wind is: {2}mph \n
''{4}'' \n
\t -{5}

""".format(
    current.temperature,
    current.apparentTemperature,
    current.windSpeed,
    summary,
    quote,
    author
)
try:
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    # server.starttls()
    server.login(user, pwd)
    print("Server Logged In")

    server.sendmail(user, recipient, body)
    server.close()
    print("Email has been sent")
except Exception as e: 
    print("There was an error: \n"+str(e))
    


