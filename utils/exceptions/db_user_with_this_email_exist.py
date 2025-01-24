from utils.i18n import Translator


class DBUserWithThisEmailExist(Exception):
    def __init__(self):
        self.message = Translator.translate('Exceptions.DBUserWithThisEmailExist')
        super().__init__(self.message)
