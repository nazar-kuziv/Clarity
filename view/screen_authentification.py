from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox

from utils.i18n import Translator
from view.screen_login import ScreenLogin
from view.screen_registration import ScreenRegistration
from view.widgets.label_with_clickable_text import LabelWithClickableText


class ScreenAuthentification(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(620, 920)
        self.setStyleSheet("background-color: #FFF8EA;")
        self.set_login_screen()

    def set_login_screen(self):
        try:
            self.setWindowTitle(Translator.translate('WindowTitles.Login'))
            self.main_widget = QWidget()
            self.main_widget.setContentsMargins(0, 0, 0, 0)
            self.main_widget.setContentsMargins(0, 0, 0, 0)
            self.main_layout = QVBoxLayout()
            self.main_layout.setSpacing(0)
            self.main_layout.setContentsMargins(0, 0, 0, 0)
            self.main_widget.setLayout(self.main_layout)
            self.setCentralWidget(self.main_widget)

            self.login_widget = ScreenLogin(self.load_main_screen)
            self.main_layout.addWidget(self.login_widget)
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
            self.main_layout.addWidget(label_sign_up, alignment=Qt.AlignHCenter)
            self.setCentralWidget(self.main_widget)
        except Exception as e:
            self.show_error(str(e))

    def set_registration_screen(self):
        try:
            self.setWindowTitle(Translator.translate('WindowTitles.Registration'))
            self.main_widget = QWidget()
            self.main_widget.setContentsMargins(0, 0, 0, 0)
            self.main_widget.setContentsMargins(0, 0, 0, 0)
            self.main_layout = QVBoxLayout()
            self.main_layout.setSpacing(0)
            self.main_layout.setContentsMargins(0, 0, 0, 0)
            self.main_widget.setLayout(self.main_layout)
            self.setCentralWidget(self.main_widget)

            self.registration_widget = ScreenRegistration(self.load_main_screen)
            self.main_layout.addWidget(self.registration_widget)
            self.label_sing_in = LabelWithClickableText(Translator.translate('Labels.HaveAnAccount'),
                                                        Translator.translate('Labels.SingIn'),
                                                        self.set_login_screen)
            self.label_sing_in.set_base_text_style("""
                   QLabel {
                       font-family: Outfit;
                       color: #222222;
                       font-size: 16px;
                   }
               """)
            self.label_sing_in.set_clickable_text_style("""
                   QLabel {
                       font-family: Outfit;
                       font-weight: bold;
                       font-size: 16px;
                   }
               """)
            self.label_sing_in.setContentsMargins(0, 0, 0, 80)
            # noinspection PyUnresolvedReferences
            self.main_layout.addWidget(self.label_sing_in, alignment=Qt.AlignHCenter)
            self.setCentralWidget(self.main_widget)
        except Exception as e:
            self.show_error(str(e))

    def load_main_screen(self):
        self.close()
        pass

    def show_error(self, error):
        # noinspection PyArgumentList
        QMessageBox.critical(self, Translator.translate('WindowTitles.Error'), str(error))
