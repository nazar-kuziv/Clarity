from utils.i18n import Translator


class MailUnableToSend(Exception):
    def __init__(self):
        self.message = Translator.translate('Exceptions.MailUnableToSend')
        super().__init__(self.message)
