import smtplib
import * from config


user = "starbuckswork01@gmail.com"
password = pwd
recipient = "grayson.stream@gmail.com"


body = """
Hello Sailor from python code!
"""


try:
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    # server.starttls()
    server.login(user, password)
    print("Server Logged In")
    server.sendmail(user, recipient, body)
    server.close()
    print("Email has been sent")
except:
    print("Something went wrong...")

/home/pi/Documents/weatherMail/sendMail.py
