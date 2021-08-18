import smtplib
from keys import email_, password # your should import your keys to your mail


title = 'some title text'
to_email = 'some@gmail.com'
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
