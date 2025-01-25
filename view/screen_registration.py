from PySide6.QtCore import Qt
from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy, QMessageBox

from controller.controller_registration import ControllerRegistration
from utils.i18n import Translator
from view.widgets.app_header import AppHeader
from view.widgets.button_basic import ButtonBasic
from view.widgets.input_validated_label import InputValidatedLabel


class ScreenRegistration(QWidget):
    def __init__(self, after_login_callback=None, parent=None):
        super().__init__(parent)
        try:
            self._controller = ControllerRegistration(self, after_login_callback)
        except Exception as e:
            self.show_error(str(e))
            self.close()
            self.deleteLater()
            return
        self._main_layout = QVBoxLayout()
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setSpacing(0)
        self.setLayout(self._main_layout)
        logo_app_name = AppHeader()
        logo_app_name.setStyleSheet("margin-top: 39px; margin-right: 11px;")
        # noinspection PyUnresolvedReferences
        self._main_layout.addWidget(logo_app_name, alignment=Qt.AlignRight | Qt.AlignTop)
        create_your_acc_label = QLabel(Translator.translate('Labels.CreateYourAccount'))
        create_your_acc_label.setStyleSheet("""
            QLabel {
                font-family: Outfit;
                font-weight: bold;
                color: #4F6F53;
                font-size: 52px;
                margin-top: 32px;
            }
        """)
        # noinspection PyUnresolvedReferences
        create_your_acc_label.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        # noinspection PyUnresolvedReferences
        self._main_layout.addWidget(create_your_acc_label, alignment=Qt.AlignTop | Qt.AlignHCenter)

        self._input_name = InputValidatedLabel(Translator.translate('Labels.InputYourName'))
        self._input_name.setContentsMargins(0, 32, 0, 0)
        self._input_name.setFixedSize(448, 100)
        # noinspection PyUnresolvedReferences
        self._main_layout.addWidget(self._input_name, alignment=Qt.AlignHCenter)

        self._input_last_name = InputValidatedLabel(Translator.translate('Labels.InputYourLastName'))
        self._input_last_name.setContentsMargins(0, 17, 0, 0)
        self._input_last_name.setFixedSize(448, 85)
        # noinspection PyUnresolvedReferences
        self._main_layout.addWidget(self._input_last_name, alignment=Qt.AlignHCenter)

        self._input_mail = InputValidatedLabel(Translator.translate('Labels.InputYourEmail'))
        self._input_mail.setContentsMargins(0, 17, 0, 0)
        self._input_mail.setFixedSize(448, 85)
        # noinspection PyUnresolvedReferences
        self._main_layout.addWidget(self._input_mail, alignment=Qt.AlignHCenter)

        self._input_password = InputValidatedLabel(Translator.translate('Labels.InputYourPassword'))
        self._input_password.set_password_mode()
        self._input_password.setContentsMargins(0, 17, 0, 0)
        self._input_password.setFixedSize(448, 85)
        #  noinspection PyUnresolvedReferences
        self._main_layout.addWidget(self._input_password, alignment=Qt.AlignHCenter)

        self._repeat_password = InputValidatedLabel(Translator.translate('Labels.EnterPasswordAgain'))
        self._repeat_password.setContentsMargins(0, 17, 0, 23)
        self._repeat_password.setFixedSize(448, 106)
        self._repeat_password.set_password_mode()
        #  noinspection PyUnresolvedReferences
        self._main_layout.addWidget(self._repeat_password, alignment=Qt.AlignHCenter)

        self._error_label = QLabel(Translator.translate('Labels.UnableToLogin'))
        self._error_label.setStyleSheet("""
            QLabel {
                font-family: Outfit;
                color: #AA4A44;
                font-size: 15px;
            }
        """)
        self._error_label.setFixedSize(431, 57)
        self._error_label.setContentsMargins(0, 0, 0, 23)
        self._error_label.setVisible(False)
        # noinspection PyUnresolvedReferences
        self._main_layout.addWidget(self._error_label, alignment=Qt.AlignHCenter)

        btn_register = ButtonBasic(Translator.translate('Buttons.Register'))
        btn_register.clicked.connect(self._controller.register)
        btn_register.setFixedSize(394, 60)
        btn_register.setContentsMargins(0, 20, 0, 38)
        # noinspection PyUnresolvedReferences
        self._main_layout.addWidget(btn_register, alignment=Qt.AlignHCenter)
        enter_for_login = QShortcut(QKeySequence("Return"), self)
        enter_for_login.activated.connect(self._controller.register)
        self._main_layout.addStretch()

    def get_name(self) -> str:
        return self._input_name.get_text()

    def get_last_name(self) -> str:
        return self._input_last_name.get_text()

    def get_mail(self) -> str:
        return self._input_mail.get_text()

    def get_password(self) -> str:
        return self._input_password.get_text()

    def get_repeat_password(self) -> str:
        return self._repeat_password.get_text()

    def set_valid_name(self, is_valid: bool):
        self._input_name.set_valid_style(is_valid)

    def set_valid_last_name(self, is_valid: bool):
        self._input_last_name.set_valid_style(is_valid)

    def set_valid_password(self, is_valid: bool):
        self._input_password.set_valid_style(is_valid)
        self._repeat_password.set_valid_style(is_valid)

    def set_valid_mail(self, is_valid: bool):
        self._input_mail.set_valid_style(is_valid)

    def set_valid_label(self, is_valid: bool, error_message: str = ''):
        self._error_label.setVisible(not is_valid)
        self._error_label.setText(error_message)

    def show_error(self, error):
        # noinspection PyArgumentList
        QMessageBox.critical(self, Translator.translate('WindowTitles.Error'), str(error))
