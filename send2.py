import smtplib
from configs import *


user = "starbuckswork01@gmail.com"
recipient = "grayson.stream@gmail.com"

body = """\
Subject: Daily Weather Email
Currently the weather is: {0} degress \n
It Feels like: {1} degress\n
The wind is: {2}mph\n
Summary for the day: {3}
""".format()

try:
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    # server.starttls()
    server.login(user, pwd)
    print("Server Logged In")

    server.sendmail(user, recipient, body)
    server.close()
    print("Email has been sent")
except:
    print("Something went wrong...")

