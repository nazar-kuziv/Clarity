from PySide6.QtCore import Qt
from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy, QMessageBox

from controller.controller_login import ControllerLogin
from utils.i18n import Translator
from view.widgets.app_header import AppHeader
from view.widgets.button_basic import ButtonBasic
from view.widgets.input_validated_label import InputValidatedLabel


class ScreenLogin(QWidget):
    def __init__(self, after_login_callback=None, parent=None):
        super().__init__(parent)
        self._controller = ControllerLogin(self, after_login_callback)
        self._main_layout = QVBoxLayout()
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setSpacing(0)
        self.setLayout(self._main_layout)
        logo_app_name = AppHeader()
        logo_app_name.setStyleSheet("margin-top: 39px; margin-right: 11px;")
        # noinspection PyUnresolvedReferences
        self._main_layout.addWidget(logo_app_name, alignment=Qt.AlignRight | Qt.AlignTop)
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
        self._main_layout.addWidget(nice_to_see_you_label, alignment=Qt.AlignTop | Qt.AlignHCenter)
        login_label = QLabel(Translator.translate('Labels.LoginIntoYourAccount'))
        login_label.setStyleSheet("""
            QLabel {
                font-family: Outfit;
                color: #222222;
                font-size: 30px;
            }
        """)
        # noinspection PyUnresolvedReferences
        self._main_layout.addWidget(login_label, alignment=Qt.AlignTop | Qt.AlignHCenter)
        self._input_mail = InputValidatedLabel(Translator.translate('Labels.InputYourEmail'))
        self._input_mail.setContentsMargins(0, 57, 0, 45)
        self._input_mail.setFixedSize(448, 186)
        # noinspection PyUnresolvedReferences
        self._main_layout.addWidget(self._input_mail, alignment=Qt.AlignHCenter)
        self._input_password = InputValidatedLabel(Translator.translate('Labels.InputYourPassword'))
        self._input_password.set_password_mode()
        self._input_password.setContentsMargins(0, 0, 0, 43)
        self._input_password.setFixedSize(448, 127)
        #  noinspection PyUnresolvedReferences
        self._main_layout.addWidget(self._input_password, alignment=Qt.AlignHCenter)

        self._error_label = QLabel(Translator.translate('Labels.UnableToLogin'))
        self._error_label.setStyleSheet("""
            QLabel {
                font-family: Outfit;
                color: #AA4A44;
                font-size: 15px;
            }
        """)
        self._error_label.setFixedSize(431, 95)
        self._error_label.setContentsMargins(0, 0, 0, 57)
        self._error_label.setVisible(False)
        # noinspection PyUnresolvedReferences
        self._main_layout.addWidget(self._error_label, alignment=Qt.AlignHCenter)

        btn_login = ButtonBasic(Translator.translate('Buttons.Login'))
        btn_login.clicked.connect(self._controller.login)
        btn_login.setFixedSize(394, 60)
        btn_login.setContentsMargins(0, 0, 0, 45)
        # noinspection PyUnresolvedReferences
        self._main_layout.addWidget(btn_login, alignment=Qt.AlignHCenter)
        enter_for_login = QShortcut(QKeySequence("Return"), self)
        enter_for_login.activated.connect(self._controller.login)
        self._main_layout.addStretch()

    def get_mail(self) -> str:
        return self._input_mail.get_text()

    def get_password(self) -> str:
        return self._input_password.get_text()

    def set_valid_password(self, is_valid: bool):
        self._input_password.set_valid_style(is_valid)

    def set_valid_mail(self, is_valid: bool):
        self._input_mail.set_valid_style(is_valid)

    def set_valid_label(self, is_valid: bool):
        self._error_label.setVisible(not is_valid)

    def show_error(self, error):
        # noinspection PyArgumentList
        QMessageBox.critical(self, Translator.translate('WindowTitles.Error'), str(error))
