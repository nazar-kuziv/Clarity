from utils.i18n import Translator


class XlsxExportFailed(Exception):
    def __init__(self):
        self.message = Translator.translate('Exceptions.XlsxExportFailed')
        super().__init__(self.message)
