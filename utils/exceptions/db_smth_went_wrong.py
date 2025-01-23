from utils.i18n import Translator


class DBSmthWentWrong(Exception):
    def __init__(self):
        self.message = Translator.translate('Exceptions.DBSmthWentWrong')
        super().__init__(self.message)
