import logging
import shutil
import sys

from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QMessageBox

from utils.environment import Environment
from utils.i18n import Translator
from utils.sentiment import Sentiment
from view.screen_authentification import ScreenAuthentification


def add_fonts():
    QtGui.QFontDatabase.addApplicationFont(Environment.resource_path('static/fonts/Junge.ttf'))
    QtGui.QFontDatabase.addApplicationFont(Environment.resource_path('static/fonts/Outfit.ttf'))


def try_delete_tmp_dir():
    try:
        tmp_path = Environment.resource_path('tmp')
        shutil.rmtree(tmp_path)
    except Exception:
        pass


if __name__ == '__main__':
    try:
        Translator.initialize('pl')

        app = QApplication(sys.argv)
        add_fonts()
        app.setWindowIcon(QtGui.QIcon(Environment.resource_path('static/images/logo.png')))

        logging.disable(logging.CRITICAL)

        login_screen = ScreenAuthentification()
        # us = UserSession()
        # us.set_user_data(1, '', '', '')
        # login_screen = ScreenMain()
        # login_screen.showMaximized()

        try:
            sentiment = Sentiment()
        except Exception as e:
            # noinspection PyArgumentList
            QMessageBox.critical(None, Translator.translate('WindowTitles.Error'),
                                 Translator.translate('Errors.SentimentModelLoadingError'))

        login_screen.show()
        app.exec()
        try_delete_tmp_dir()
    except KeyboardInterrupt:
        exit(0)
