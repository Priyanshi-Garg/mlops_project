

import smtplib, ssl

port = 465 # FOR SSL
smtp_server = "smtp.gmail.com"
sender_email = "gargpriyanshi39@gmail.com"
reciever_email = "gargpriyanshi39@gmail.com"
password = <user_password>
message = """\
Subject: Mlops_project

Congratulations your model has been trained successfully and you achieved accuracy more than 80%"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, reciever_email, message)
