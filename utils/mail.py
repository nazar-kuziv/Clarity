import mimetypes
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import dotenv_values

from utils.environment import Environment
from utils.exceptions.mail_unable_to_init_service import MailUnableToInitService
from utils.exceptions.mail_unable_to_send import MailUnableToSend


class SMTPConnectionMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            instance.connect()
            cls._instances[cls] = instance
        return cls._instances[cls]


class MailService(metaclass=SMTPConnectionMeta):

    def connect(self):
        try:
            env_vars = dotenv_values(Environment.resource_path(".env"))
            self._from_email = env_vars.get("MAIL_ADDRESS")
            self._app_password = env_vars.get("EMAIL_APP_PASSWORD")
            self._smtp_server = 'smtp.gmail.com'
            self._smtp_port = 587
            self._server = smtplib.SMTP(self._smtp_server, self._smtp_port)
            self._server.starttls()
            self._server.login(self._from_email, self._app_password)
        except Exception:
            raise MailUnableToInitService()

    def send_mail(self, to_email: str, subject: str, body: str):
        try:
            msg = MIMEText(body, 'plain')
            msg['From'] = self._from_email
            msg['To'] = to_email
            msg['Subject'] = subject

            self._server.sendmail(self._from_email, to_email, msg.as_string())
        except Exception:
            raise MailUnableToSend()

    def send_mail_with_attachments(self, to_email: str, subject: str, body: str, attachments: list[str]):
        try:
            msg = MIMEMultipart()
            msg['From'] = self._from_email
            msg['To'] = to_email
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))

            for file_path in attachments:
                content_type, encoding = mimetypes.guess_type(file_path)
                if content_type is None or encoding is not None:
                    content_type = 'application/octet-stream'

                main_type, sub_type = content_type.split('/', 1)

                with open(file_path, 'rb') as f:
                    part = MIMEBase(main_type, sub_type)
                    part.set_payload(f.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(file_path)}"')
                    msg.attach(part)

            self._server.sendmail(self._from_email, to_email, msg.as_string())
        except Exception:
            raise MailUnableToSend()
