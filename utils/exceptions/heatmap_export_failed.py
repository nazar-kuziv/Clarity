from utils.i18n import Translator


class HeatmapExportFailed(Exception):
    def __init__(self):
        self.message = Translator.translate('Exceptions.HeatmapExportFailed')
        super().__init__(self.message)
