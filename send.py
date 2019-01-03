import smtplib, ssl
import requests, os, sys
import praw 
from darksky import forecast
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

from configs import *


smtp_server = "smtp.gmail.com"
port = 465
reddit = praw.Reddit(client_id=reddit_id,
                     client_secret=reddit_secret,
                     user_agent='testscript by /u/skysetter')

def redditTitle(sub, limit =1):
    for text in reddit.subreddit(sub).top('day', limit=limit):
        title = text.title
        return

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



lat = "47.57070050000001"
lon =  "-122.38715259999998"
forecast = forecast(api_key, lat, lon)

icon = forecast.currently.icon
temperature = forecast.currently.temperature
feelsLike = forecast.currently.apparentTemperature
windSpeed = forecast.currently.windSpeed
summary = forecast.hourly.summary


sender_email = "daily.weather.email@gmail.com"
receiver_email  = "grayson.stream@gmail.com"

message = MIMEMultipart("alternative")
message["Subject"] = "Daily Weather Email"
message["From"] = sender_email
message["To"] = receiver_email





dirPath = os.path.dirname(os.path.realpath(__file__))

if sys.platform == "win32":

    weatherImg= "{0}\\images\\{1}.png".format(dirPath,icon)
    tilImg = "{0}\\images\\{1}.png".format(dirPath,"til")
    quoteImg = "{0}\\images\\{1}.png".format(dirPath,"quote")

else:
    weatherImg= "{0}/images/{1}.png".format(dirPath,icon)
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

html = """<head>
    <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
    <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>
    <script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
</head>
<body>
    <div id="mailsub" class="notification" align="center">
        <table width="100%" border="0" cellspacing="0" cellpadding="0" style="min-width: 320px;">
            <tr>
                <td align="center" bgcolor="#eff3f8">
            <tr>
                <td align="center" bgcolor="#fbfcfd">
                    <table width="90%" border="0" cellspacing="0" cellpadding="0">
                        <tr>
                            <td align="center">
                                <!-- padding -->
                                    <img src="cid:image1" alt="weather-icon" border="0" style="width:120px;height:120px;" />
                                <!-- padding -->
                                <div style="height: 10px; line-height: 10px; font-size: 10px;"> </div>
                            </td>
                        </tr>
                        <td align="center">
                        <font face="Arial, Helvetica, sans-serif" size="3" color="#8A2BE2" style="font-size: 14px;" >
								<strong style="font-family: Arial, Helvetica, sans-serif; font-size: 14px; color: #8A2BE2;">
									<a href="#2" target="_blank" style="color: #8A2BE2; text-decoration: none;">WEATHER</a>
								</strong></font>
                        </td>
                        <tr>
                            <td align="center">
                                <div style="line-height: 12px;">
                                    <font face="Arial, Helvetica, sans-serif" size="5" color="#57697e" style="font-size: 16px;">
                                        <span style="font-family: Arial, Helvetica, sans-serif; font-size: 16px; color: #57697e;">
                                            <p>Daily Summary: {3}</p>
                                            <p>Current Temperature: {0} degrees</p>
                                            <p>Feels like: {1} degrees</p>
                                            <p>Wind Speed: {2}mph</p>
                                        </span></font>
                                </div>
                                <!-- padding -->
                                <div style="height: 10px; line-height: 10px; font-size: 10px;"> </div>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
            <!--content 1 END-->
            <tr>
                <td align="center" bgcolor="#fbfcfd">
                    <table width="90%" border="0" cellspacing="0" cellpadding="0">
                        <tr>
                            <td align="center">
                                <!-- padding -->
                                <div style="height: 10px; line-height: 10px; font-size: 10px;"> </div>
                                <div style="line-height: 22px;">
                                    <img src="cid:image2" alt="quote-icon" border="0" style="width:220px;height:120px;" />
                                </div>
                                <!-- padding -->
                                <div style="height: 10px; line-height: 10px; font-size: 10px;"> </div>
                            </td>
                        </tr>
                         <td align="center">
                        <font face="Arial, Helvetica, sans-serif" size="3" color="#8A2BE2" style="font-size: 14px;" >
								<strong style="font-family: Arial, Helvetica, sans-serif; font-size: 14px; color: #8A2BE2;">
									<a href="#2" target="_blank" style="color: #8A2BE2; text-decoration: none;">TODAY I LEARNED</a>
								</strong></font>
                        </td>
                        <tr>
                            <td align="center">
                                <div style="line-height: 12px;">
                                    <font face="Arial, Helvetica, sans-serif" size="5" color="#57697e" style="font-size: 22px;">
                                        <span style="font-family: Arial, Helvetica, sans-serif; font-size: 16px; color: #57697e;">
                                            {6}
                                        </span></font>q
                                </div>
                                <!-- padding -->
                                <div style="height: 10px; line-height: 10px; font-size: 10px;"> </div>
                            </td>
                        </tr>
                        <tr>
                            <td align="center">
                                <div style="line-height: 24px;">
                                </div>
                                <!-- padding -->
                                <div style="height: 10px; line-height: 10px; font-size: 10px;"> </div>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
            <!--content 1a END-->
            <tr>
                <td align="center" bgcolor="#fbfcfd">
                    <table width="90%" border="0" cellspacing="0" cellpadding="0">
                        <tr>
                            <td align="center">
                                <!-- padding -->
                                <div style="height: 10px; line-height: 10px; font-size: 10px;"> </div>
                                <div style="line-height: 22px;">
                                    <img src="cid:image3" alt="til-icon" border="0" style="width:120px;height:120px;" />
                                </div>
                                <!-- padding -->
                                <div style="height: 10px; line-height: 10px; font-size: 10px;"> </div>
                            </td>
                        </tr>
                        <td align="center">
                        <font face="Arial, Helvetica, sans-serif" size="3" color="#8A2BE2" style="font-size: 14px;" >
								<strong style="font-family: Arial, Helvetica, sans-serif; font-size: 14px; color: #8A2BE2;">
									<a href="#2" target="_blank" style="color: #8A2BE2; text-decoration: none;">QUOTE OF THE DAY</a>
								</strong></font>
                        </td>
                        <tr>
                            <td align="center">
                                <div style="line-height: 12px;">
                                    <font face="Arial, Helvetica, sans-serif" size="5" color="#57697e" style="font-size: 22px;">
                                        <span style="font-family: Arial, Helvetica, sans-serif; font-size: 16px; color: #57697e;">
                                            {4}
                                            <p>-{5}</p>
                                        </span></font>
                                </div>
                                <!-- padding -->
                                <div style="height: 40px; line-height: 40px; font-size: 10px;"> </div>
                            </td>
                        </tr>
                        <tr>
                            <td align="center">
                                <div style="line-height: 24px;">
                                </div>
                                <!-- padding -->
                                <div style="height: 10px; line-height: 10px; font-size: 10px;"> </div>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
            <!--content 1b END-->
        </td>
        </tr>
        </table>
</body>
</html>""".format(
    temperature,
    feelsLike,
    windSpeed,
    summary,
    quote,
    author,
    redditTitle('todayilearned')
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
