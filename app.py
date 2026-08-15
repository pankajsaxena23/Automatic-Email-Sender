import smtplib

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
server.login(sender_email, "spgy rfsj xpbx pxhn")

for receiver_email in receivers:
    server.sendmail(sender_email, receiver_email, text)
    print(f"Email sent to {receiver_email}")

server.quit()
