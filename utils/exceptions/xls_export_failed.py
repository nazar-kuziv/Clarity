from utils.i18n import Translator


class XlsExportFailed(Exception):
    def __init__(self):
        self.message = Translator.translate('Exceptions.XlsExportFailed')
        super().__init__(self.message)
