from utils.i18n import Translator


class DBUnableToGetData(Exception):
    def __init__(self):
        self.message = Translator.translate('Exceptions.DBUnableToGetData')
        super().__init__(self.message)
