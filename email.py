import smtplib


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password-here')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    to = "sendmailto@gmail.com"
    content = "content to send"
    sendEmail(to, content)
