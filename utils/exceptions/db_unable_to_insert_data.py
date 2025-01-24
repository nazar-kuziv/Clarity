from utils.i18n import Translator


class DBUnableToInsertData(Exception):
    def __init__(self):
        self.message = Translator.translate('Exceptions.DBUnableToInsertData')
        super().__init__(self.message)
