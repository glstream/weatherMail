# -*- coding: utf-8 -*-
import forecastio
import smtplib, ssl
import requests, os, sys
import praw 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

from configs import *
from emailTemplate import *

smtp_server = "smtp.gmail.com"
port = 465
reddit = praw.Reddit(client_id=reddit_id,
                     client_secret=reddit_secret,
                     user_agent='testscript by /u/skysetter')


lat = "47.57070050000001"
lng =  "-122.38715259999998"


url = 'https://quotes.rest/qod'
res = requests.get(url)
resData = res.json()

try: 
    resData['contents']['quotes']
    data = resData['contents']['quotes']
except Exception as e:
    print("Couldn't get quote needed using backup quote")
    data = [{u'category': u'inspire', u'permalink': u'https://theysaidso.com/quote/74RZL1_lOJ5uScr4h8ntCgeF/napoleon-hill-effort-only-fully-releases-its-reward-after-a-person-refuses-to-qu', u'tags': [u'effort', u'inspire'], u'quote': u'Effort only fully releases its reward after a person refuses to quit.', u'author': u'Napoleon Hill', u'length': u'69', u'background': u'https://theysaidso.com/img/bgs/man_on_the_mountain.jpg', u'date': u'2018-12-23', u'title': u'Inspiring Quote of the day', u'id': u'74RZL1_lOJ5uScr4h8ntCgeF'}]

quote = data[0]["quote"]
author = data[0]["author"]

forecast = forecastio.load_forecast(api_key, lat, lng)

current = forecast.currently()
hourly =  forecast.hourly()



sender_email = "daily.weather.email@gmail.com"
receiver_email  = "grayson.stream@gmail.com"

message = MIMEMultipart("alternative")
message["Subject"] = "Daily Weather Email"
message["From"] = sender_email
message["To"] = receiver_email

s = hourly.summary
summary = s.encode('ascii', errors='ignore').decode()

for text in reddit.subreddit('todayilearned').top('day', limit=1):
    encTitle = text.title
    title = encTitle.encode('ascii', errors='ignore').decode()

dirPath = os.path.dirname(os.path.realpath(__file__))

if sys.platform == "win32":

    weatherImg= "{0}\\images\\{1}.png".format(dirPath,current.icon)
    tilImg = "{0}\\images\\{1}.png".format(dirPath,"til")
    quoteImg = "{0}\\images\\{1}.png".format(dirPath,"quote")

else:
    weatherImg= "{0}/images/{1}.png".format(dirPath,current.icon)
    tilImg = "{0}/images/{1}.png".format(dirPath,"til")
    quoteImg = "{0}/images/{1}.png".format(dirPath,"quote")

try: 
    # This example assumes the image is in the current directory
    fp = open(weatherImg, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
except Exception as e:
    print("Dont have icon for this weather")
    imageFile= "{0}/images/{1}.png".format(dirPath,"platypus")
    fp = open(imageFile, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()


fp2 = open(tilImg, 'rb')
msgImage2 = MIMEImage(fp2.read())
fp2.close()


fp3 = open(quoteImg, 'rb')
msgImage3 = MIMEImage(fp3.read())
fp3.close()

html.format(
    current.temperature,
    current.apparentTemperature,
    current.windSpeed,
    summary,
    quote,
    author,
    title
)

part1 = MIMEText(html, "html")
msgImage.add_header('Content-ID', '<image1>')
msgImage2.add_header('Content-ID', '<image2>')
msgImage3.add_header('Content-ID', '<image3>')

message.attach(part1)
message.attach(msgImage)
message.attach(msgImage2)
message.attach(msgImage3)

try:
   
    server = smtplib.SMTP_SSL(smtp_server, port)
    server.ehlo()
    # server.starttls()
    server.login(sender_email, pwd)
    print("Server Logged In")

    server.sendmail(sender_email, receiver_email , message.as_string())
    server.close()
    print("Email has been sent")

except Exception as e: 
    print("There was an error: \n"+str(e))
    


