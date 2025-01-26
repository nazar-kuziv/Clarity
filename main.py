import sys

from PySide6 import QtGui
from PySide6.QtWidgets import QApplication

from utils.environment import Environment
from utils.i18n import Translator
from utils.user_session import UserSession
from view.screen_authentification import ScreenAuthentification
from view.screen_main import ScreenMain
from view.widgets.widget_diary_entry import WidgetDiaryEntry


def add_fonts():
    QtGui.QFontDatabase.addApplicationFont(Environment.resource_path('static/fonts/Junge.ttf'))
    QtGui.QFontDatabase.addApplicationFont(Environment.resource_path('static/fonts/Outfit.ttf'))


try:
    Translator.initialize('pl')

    app = QApplication(sys.argv)
    add_fonts()
    app.setWindowIcon(QtGui.QIcon(Environment.resource_path('static/images/logo.png')))

    login_screen = ScreenAuthentification()
    login_screen.show()
    app.exec()
except KeyboardInterrupt:
    exit(0)
