from utils.i18n import Translator


class MailUnableToInitService(Exception):
    def __init__(self):
        self.message = Translator.translate('Exceptions.MailUnableToInitService')
        super().__init__(self.message)
