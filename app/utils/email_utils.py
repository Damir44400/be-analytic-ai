import smtplib
from email.mime.text import MIMEText
from app.config import RootUserEmail

import html


def stylizing_email(message):
    escaped_message = html.escape(message)
    email_style = '''
        <!DOCTYPE html>
        <html>
            <head>
                <link rel="stylesheet" type="text/css" hs-webfonts="true" href="https://fonts.googleapis.com/css?family=Lato|Lato:i,b,bi">
                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
            </head>
            <body bgcolor="#F5F8FA" style="width: 100%; font-family: 'Lato', sans-serif; font-size: 18px; margin: 0; padding: 0;">
                <div id="email" style="max-width: 600px; margin: auto; background-color: #fff; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); border-radius: 8px; overflow: hidden;">
                    <div id="header" style="background-color: #00A4BD; color: white; text-align: center; padding: 20px 0;">
                        <h1 style="font-size: 36px; margin: 0;">Your Code to Reset Password</h1>
                    </div>
                    <div id="content" style="padding: 30px 30px 30px 60px;">
                        <center>
                            <h2 style="font-size: 24px; font-weight: 900; margin-bottom: 10px;">{}</h2>
                        </center>
                        <p style="font-weight: 100; margin-top: 0;">Keep it confidential. Don't show it to anyone.</p>
                    </div>
                </div>
            </body>
        </html>
    '''.format(escaped_message)

    return email_style


class SendEmail:
    def __init__(self, to, message):
        self.to = to
        self.__msg = MIMEText(stylizing_email(message), 'html')
        self.__sender = RootUserEmail()

    def send_email(self):
        self.__msg['Subject'] = "AniTolqyn"
        self.__msg['From'] = self.__sender.ROOT_EMAIL
        self.__msg['To'] = self.to
        host, port = self.__get_host_and_port()
        try:
            with smtplib.SMTP_SSL(host, port) as smtp_server:
                smtp_server.login(self.__sender.ROOT_EMAIL, self.__sender.ROOT_PASSWORD)
                smtp_server.sendmail(self.__sender.ROOT_EMAIL, self.to, self.__msg.as_string())
            return "send"
        except smtplib.SMTPException as e:
            raise "Internal server error"

    def __get_host_and_port(self):
        host, port = "smtp.gmail.com", 465
        if self.__sender.ROOT_EMAIL.endswith("@mail.ru"):
            host = "smtp.mail.com"
        return [host, port]