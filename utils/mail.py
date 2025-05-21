import base64
from email.mime.text import MIMEText

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from utils.environment import Environment
from utils.exceptions.mail_unable_to_init_service import MailUnableToInitService
from utils.exceptions.mail_unable_to_send import MailUnableToSend


class MailServiceMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            instance.initialize()
            cls._instances[cls] = instance
        return cls._instances[cls]


class MailService(metaclass=MailServiceMeta):

    def initialize(self):
        try:
            scopes = ["https://www.googleapis.com/auth/gmail.addons.current.action.compose"]
            creds = Credentials.from_authorized_user_file(Environment.resource_path("token.json"), scopes)
            self.service = build("gmail", "v1", credentials=creds)
        except Exception:
            raise MailUnableToInitService()

    def send_mail(self, to_email: str, subject: str, body: str, from_email: str):
        try:
            message = MIMEText(body)
            message["to"] = to_email
            message["from"] = from_email
            message["subject"] = subject

            raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

            self.service.users().messages().send(
                userId="me",
                body={"raw": raw_message}
            ).execute()
        except Exception:
            raise MailUnableToSend()
