from utils.i18n import Translator


class DBUnableToConnect(Exception):
    def __init__(self):
        self.message = Translator.translate('Exceptions.DBUnableToConnect')
        super().__init__(self.message)