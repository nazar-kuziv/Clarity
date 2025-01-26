from utils.i18n import Translator


class DBUnableToAlterData(Exception):
    def __init__(self):
        self.message = Translator.translate('Exceptions.DBUnableToAlterData')
        super().__init__(self.message)
