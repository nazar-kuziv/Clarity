from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox

from utils.i18n import Translator
from view.screen_login import ScreenLogin
from view.screen_main import ScreenMain
from view.screen_registration import ScreenRegistration
from view.widgets.label_with_clickable_text import LabelWithClickableText


class ScreenAuthentification(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(620, 920)
        self.setObjectName('ScreenAuthentification')
        self.setStyleSheet("#ScreenAuthentification{background-color: #FFF8EA;}")
        self.set_login_screen()

    def set_login_screen(self):
        try:
            self.setWindowTitle(Translator.translate('WindowTitles.Login'))
            self._main_widget = QWidget()
            self._main_widget.setContentsMargins(0, 0, 0, 0)
            self._main_widget.setContentsMargins(0, 0, 0, 0)
            self._main_layout = QVBoxLayout()
            self._main_layout.setSpacing(0)
            self._main_layout.setContentsMargins(0, 0, 0, 0)
            self._main_widget.setLayout(self._main_layout)
            self.setCentralWidget(self._main_widget)

            self._login_widget = ScreenLogin(self.load_main_screen)
            self._main_layout.addWidget(self._login_widget)
            label_sign_up = LabelWithClickableText(Translator.translate('Labels.DontHaveAnAccount'),
                                                   Translator.translate('Labels.SignUpNow'),
                                                   self.set_registration_screen)
            label_sign_up.set_base_text_style("""
                       QLabel {
                           font-family: Outfit;
                           color: #222222;
                           font-size: 16px;
                       }
                   """)
            label_sign_up.set_clickable_text_style("""
                       QLabel {
                           font-family: Outfit;
                           font-weight: bold;
                           font-size: 16px;
                       }
                   """)
            label_sign_up.setContentsMargins(0, 20, 0, 111)
            # noinspection PyUnresolvedReferences
            self._main_layout.addWidget(label_sign_up, alignment=Qt.AlignHCenter)
            self.setCentralWidget(self._main_widget)
        except Exception as e:
            self.show_error(str(e))

    def set_registration_screen(self):
        try:
            self.setWindowTitle(Translator.translate('WindowTitles.Registration'))
            self._main_widget = QWidget()
            self._main_widget.setContentsMargins(0, 0, 0, 0)
            self._main_widget.setContentsMargins(0, 0, 0, 0)
            self._main_layout = QVBoxLayout()
            self._main_layout.setSpacing(0)
            self._main_layout.setContentsMargins(0, 0, 0, 0)
            self._main_widget.setLayout(self._main_layout)
            self.setCentralWidget(self._main_widget)

            self._registration_widget = ScreenRegistration(self.load_main_screen)
            self._main_layout.addWidget(self._registration_widget)
            self._label_sing_in = LabelWithClickableText(Translator.translate('Labels.HaveAnAccount'),
                                                         Translator.translate('Labels.SingIn'),
                                                         self.set_login_screen)
            self._label_sing_in.set_base_text_style("""
                   QLabel {
                       font-family: Outfit;
                       color: #222222;
                       font-size: 16px;
                   }
               """)
            self._label_sing_in.set_clickable_text_style("""
                   QLabel {
                       font-family: Outfit;
                       font-weight: bold;
                       font-size: 16px;
                   }
               """)
            self._label_sing_in.setContentsMargins(0, 0, 0, 80)
            # noinspection PyUnresolvedReferences
            self._main_layout.addWidget(self._label_sing_in, alignment=Qt.AlignHCenter)
            self.setCentralWidget(self._main_widget)
        except Exception as e:
            self.show_error(str(e))

    def load_main_screen(self):
        self._main_screen = ScreenMain()
        self._main_screen.showMaximized()
        self.close()
        pass

    def show_error(self, error):
        # noinspection PyArgumentList
        QMessageBox.critical(self, Translator.translate('WindowTitles.Error'), str(error))
