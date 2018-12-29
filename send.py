import forecastio
import smtplib, ssl
import requests, os, sys
import praw 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

from configs import *


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

    imageFile= "{0}\\images\\{1}.png".format(dirPath,current.icon)
else:
    imageFile= "{0}/images/{1}.png".format(dirPath,current.icon)
    
# This example assumes the image is in the current directory
fp = open(imageFile, 'rb')
msgImage = MIMEImage(fp.read())
fp.close()


html = """\
<html>
  <body>
<p><b>Summary for the day:</b> {3} </p><img src="cid:image1" style="width:50px;height:60px;">
<p>Currently the weather is: {0} degrees<p>
<p>It Feels like: {1} degress</p>
<p>The wind is: {2}mph<p>
<p>Interesting fact for today: {6} </p>
<p>Quote for day: ''{4}''</p>
<p>-{5}</p>

  </body>
</html>
""".format(
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

message.attach(part1)
message.attach(msgImage)

try:
   
    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.ehlo()
        # server.starttls()
        server.login(sender_email, pwd)
        print("Server Logged In")

        server.sendmail(sender_email, receiver_email , message.as_string())
        server.close()
        print("Email has been sent")

except Exception as e: 
    print("There was an error: \n"+str(e))
    


