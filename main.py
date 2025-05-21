import logging
import sys

from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QMessageBox

from utils.environment import Environment
from utils.i18n import Translator
from view.screen_authentification import ScreenAuthentification


def add_fonts():
    QtGui.QFontDatabase.addApplicationFont(Environment.resource_path('static/fonts/Junge.ttf'))
    QtGui.QFontDatabase.addApplicationFont(Environment.resource_path('static/fonts/Outfit.ttf'))


try:
    Translator.initialize('pl')

    app = QApplication(sys.argv)
    add_fonts()
    app.setWindowIcon(QtGui.QIcon(Environment.resource_path('static/images/logo.png')))

    logging.disable(logging.CRITICAL)

    login_screen = ScreenAuthentification()

    try:
        # sentiment = Sentiment()
        pass
    except Exception as e:
        # noinspection PyArgumentList
        QMessageBox.critical(None, Translator.translate('WindowTitles.Error'),
                             Translator.translate('Errors.SentimentModelLoadingError'))

    login_screen.show()

    app.exec()
except KeyboardInterrupt:
    exit(0)
