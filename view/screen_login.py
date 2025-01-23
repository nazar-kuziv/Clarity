from PySide6.QtCore import Qt
from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy, QMessageBox

from controller.controller_login import ControllerLogin
from utils.i18n import Translator
from view.widgets.app_header import AppHeader
from view.widgets.button_basic import ButtonBasic
from view.widgets.input_validated_label import InputValidatedLabel
from view.widgets.label_with_clickable_text import LabelWithClickableText


class ScreenLogin(QWidget):
    def __init__(self):
        super().__init__()
        try:
            self.controller = ControllerLogin(self)
        except Exception as e:
            self.show_error(str(e))
            self.close()
            self.deleteLater()
            return
        self.setObjectName("screen_login")
        self.setStyleSheet("background-color: #FFF8EA;")
        self.setFixedSize(620, 920)
        self.setWindowTitle(Translator.translate('WindowTitles.Login'))
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.setLayout(self.main_layout)
        logo_app_name = AppHeader()
        logo_app_name.setStyleSheet("margin-top: 39px; margin-right: 11px;")
        # noinspection PyUnresolvedReferences
        self.main_layout.addWidget(logo_app_name, alignment=Qt.AlignRight | Qt.AlignTop)
        nice_to_see_you_label = QLabel(Translator.translate('Labels.NiceToSeeYou'))
        nice_to_see_you_label.setStyleSheet("""
            QLabel {
                font-family: Outfit;
                font-weight: bold;
                color: #4F6F53;
                font-size: 52px;
                margin-top: 98px;
            }
        """)
        # noinspection PyUnresolvedReferences
        nice_to_see_you_label.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        # noinspection PyUnresolvedReferences
        self.main_layout.addWidget(nice_to_see_you_label, alignment=Qt.AlignTop | Qt.AlignHCenter)
        login_label = QLabel(Translator.translate('Labels.LoginIntoYourAccount'))
        login_label.setStyleSheet("""
            QLabel {
                font-family: Outfit;
                color: #222222;
                font-size: 30px;
            }
        """)
        # noinspection PyUnresolvedReferences
        self.main_layout.addWidget(login_label, alignment=Qt.AlignTop | Qt.AlignHCenter)
        self.input_mail = InputValidatedLabel(Translator.translate('Labels.InputYourEmail'))
        self.input_mail.setContentsMargins(0, 57, 0, 45)
        self.input_mail.setFixedSize(448, 172)
        self.input_mail.setObjectName("input_mail")
        # noinspection PyUnresolvedReferences
        self.main_layout.addWidget(self.input_mail, alignment=Qt.AlignHCenter)
        self.input_password = InputValidatedLabel(Translator.translate('Labels.InputYourPassword'))
        self.input_password.set_password_mode()
        self.input_password.setContentsMargins(0, 0, 0, 57)
        self.input_password.setFixedSize(448, 127)
        #  noinspection PyUnresolvedReferences
        self.main_layout.addWidget(self.input_password, alignment=Qt.AlignHCenter)

        self.error_label = QLabel(Translator.translate('Labels.UnableToLogin'))
        self.error_label.setStyleSheet("""
            QLabel {
                font-family: Outfit;
                color: #AA4A44;
                font-size: 15px;
            }
        """)
        self.error_label.setFixedSize(431, 95)
        self.error_label.setContentsMargins(0, 0, 0, 57)
        self.error_label.setVisible(False)
        # noinspection PyUnresolvedReferences
        self.main_layout.addWidget(self.error_label, alignment=Qt.AlignHCenter)

        btn_login = ButtonBasic(Translator.translate('Buttons.Login'))
        btn_login.clicked.connect(self.controller.login)
        btn_login.setFixedSize(394, 60)
        btn_login.setContentsMargins(0, 0, 0, 38)
        # noinspection PyUnresolvedReferences
        self.main_layout.addWidget(btn_login, alignment=Qt.AlignHCenter)
        self.label_sign_up = LabelWithClickableText(Translator.translate('Labels.DontHaveAnAccount'),
                                                    Translator.translate('Labels.SignUpNow'), lambda: print('test'))
        self.label_sign_up.set_base_text_style("""
            QLabel {
                font-family: Outfit;
                color: #222222;
                font-size: 16px;
            }
        """)
        self.label_sign_up.set_clickable_text_style("""
            QLabel {
                font-family: Outfit;
                font-weight: bold;
                font-size: 16px;
            }
        """)
        self.label_sign_up.setContentsMargins(0, 38, 0, 0)
        # noinspection PyUnresolvedReferences
        self.main_layout.addWidget(self.label_sign_up, alignment=Qt.AlignHCenter)
        enter_for_login = QShortcut(QKeySequence("Return"), self)
        enter_for_login.activated.connect(self.controller.login)
        self.main_layout.addStretch()

    def get_mail(self) -> str:
        return self.input_mail.get_text()

    def get_password(self) -> str:
        return self.input_password.get_text()

    def set_valid_password(self, is_valid: bool):
        self.input_password.set_valid_style(is_valid)

    def set_valid_mail(self, is_valid: bool):
        self.input_mail.set_valid_style(is_valid)

    def set_valid_label(self, is_valid: bool):
        self.error_label.setVisible(not is_valid)

    def show_error(self, error):
        # noinspection PyArgumentList
        QMessageBox.critical(self, Translator.translate('WindowTitles.Error'), str(error))
