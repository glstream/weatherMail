import forecastio
import smtplib
from configs import *

lat = "47.57070050000001"
lng =  "-122.38715259999998"


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
The wind is: {2}mph

""".format(
    current.temperature,
    current.apparentTemperature,
    current.windSpeed,
    summary,
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
    


