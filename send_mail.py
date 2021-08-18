import smtplib
from email.mime.text import MIMEText
from test2 import email_, password


title = 'something happened to the FBA_robot'
to_email = 'rasul.islyamgali@gmail.com'
message = 'Test message with Python'

BODY = "\r\n".join((
    "From: %s" % email_,
    "To: %s" % to_email,
    "Subject: %s" % title ,
    "",
    message
))

server = smtplib.SMTP('smtp.gmail.com: 587')

server.starttls()

server.login(email_, password)

server.sendmail(email_, to_email, BODY)

server.quit()