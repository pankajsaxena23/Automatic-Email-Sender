import smtplib
import os
import getpass

sender_email = input("Sender E-mail: ")

mails = int(input("How many receiver emails: "))

receivers = []
for i in range(mails):
    email = input(f"Enter receiver email {i+1}: ")
    receivers.append(email)

subject = input("Subject: ")
message = input("Message: ")

text = f"Subject: {subject}\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

password = os.environ.get("GMAIL_APP_PASSWORD") or getpass.getpass("App Password: ")
server.login(sender_email, password)

for receiver_email in receivers:
    server.sendmail(sender_email, receiver_email, text)
    print(f"Email sent to {receiver_email}")

server.quit()
