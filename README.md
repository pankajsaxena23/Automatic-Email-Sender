# 📧 Bulk Email Sender using Python

A simple Python script that sends the same email to multiple recipients using Gmail SMTP.

## 🚀 Features
- Send emails to multiple recipients
- Command-line interface
- Uses Gmail SMTP
- Custom subject and message

## 🛠️ Technologies Used
- Python 3
- smtplib
- Gmail SMTP Server

## 📂 Project Structure
```text
Bulk-Email-Sender/
│── email_sender.py
└── README.md
```

## 📋 Requirements
- Python 3.x
- Gmail account
- Gmail App Password

## ▶️ How to Run
```bash
python email_sender.py
```

## 💻 Example
```text
Sender E-mail: example@gmail.com
How many receiver emails: 2
Enter receiver email 1: user1@gmail.com
Enter receiver email 2: user2@gmail.com
Subject: Test
Message: Hello!
```

## ⚙️ How It Works
1. Collect sender email.
2. Collect recipient emails.
3. Connect to Gmail SMTP.
4. Login using App Password.
5. Send email to each recipient.

## 🔒 Security Note
Do **not** hardcode your Gmail App Password in the source code. Use environment variables or a `.env` file.

## 📌 Future Improvements
- HTML emails
- Attachments
- CSV/Excel recipients
- GUI
- Error handling

## 👨‍💻 Author
Pankaj Saxena

## 📄 License
MIT License
