import logging
import sys

from PySide6 import QtGui
from PySide6.QtWidgets import QApplication

from utils.environment import Environment
from utils.i18n import Translator
from utils.sentiment import Sentiment
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

    sentiment = Sentiment()
    sentiment.initialize()

    login_screen = ScreenAuthentification()
    login_screen.show()
    # us = UserSession()
    # us.set_user_data(1, '', '', '')
    # login_screen = ScreenMain()
    # login_screen.showMaximized()
    app.exec()
except KeyboardInterrupt:
    exit(0)
