import smtplib
from email.mime.text import MIMEText
from app.config import RootUserEmail


class SendEmail:
    def __init__(self, to, subject, message):
        self.to = to
        self.subject = subject
        self.message = message
        self.__msg = MIMEText(self.message)
        self.__sender = RootUserEmail()

    def send_email(self):
        self.__msg['Subject'] = self.subject
        self.__msg['From'] = self.__sender.ROOT_EMAIL
        self.__msg['To'] = self.to
        host, port = self.__get_host_and_port()
        try:
            with smtplib.SMTP_SSL(host, port) as smtp_server:
                smtp_server.login(self.__sender.ROOT_EMAIL, self.__sender.ROOT_PASSWORD, initial_response_ok=True)
                smtp_server.sendmail(self.__sender.ROOT_EMAIL, self.to, self.__msg.as_string())
            return "send"
        except smtplib.SMTPException as e:
            raise "Internal server error"

    def __get_host_and_port(self):
        host, port = "smtp.gmail.com", 465
        if self.__sender.ROOT_EMAIL.endswith("@mail.ru"):
            host = "smtp.mail.com"
        return [host, port]
