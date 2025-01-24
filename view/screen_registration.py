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
            self.controller = ControllerRegistration(self, after_login_callback)
        except Exception as e:
            self.show_error(str(e))
            self.close()
            self.deleteLater()
            return
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.setLayout(self.main_layout)
        logo_app_name = AppHeader()
        logo_app_name.setStyleSheet("margin-top: 39px; margin-right: 11px;")
        # noinspection PyUnresolvedReferences
        self.main_layout.addWidget(logo_app_name, alignment=Qt.AlignRight | Qt.AlignTop)
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
        self.main_layout.addWidget(create_your_acc_label, alignment=Qt.AlignTop | Qt.AlignHCenter)

        self.input_name = InputValidatedLabel(Translator.translate('Labels.InputYourName'))
        self.input_name.setContentsMargins(0, 32, 0, 0)
        self.input_name.setFixedSize(448, 100)
        # noinspection PyUnresolvedReferences
        self.main_layout.addWidget(self.input_name, alignment=Qt.AlignHCenter)

        self.input_last_name = InputValidatedLabel(Translator.translate('Labels.InputYourLastName'))
        self.input_last_name.setContentsMargins(0, 17, 0, 0)
        self.input_last_name.setFixedSize(448, 85)
        # noinspection PyUnresolvedReferences
        self.main_layout.addWidget(self.input_last_name, alignment=Qt.AlignHCenter)

        self.input_mail = InputValidatedLabel(Translator.translate('Labels.InputYourEmail'))
        self.input_mail.setContentsMargins(0, 17, 0, 0)
        self.input_mail.setFixedSize(448, 85)
        # noinspection PyUnresolvedReferences
        self.main_layout.addWidget(self.input_mail, alignment=Qt.AlignHCenter)

        self.input_password = InputValidatedLabel(Translator.translate('Labels.InputYourPassword'))
        self.input_password.set_password_mode()
        self.input_password.setContentsMargins(0, 17, 0, 0)
        self.input_password.setFixedSize(448, 85)
        #  noinspection PyUnresolvedReferences
        self.main_layout.addWidget(self.input_password, alignment=Qt.AlignHCenter)

        self.repeat_password = InputValidatedLabel(Translator.translate('Labels.EnterPasswordAgain'))
        self.repeat_password.setContentsMargins(0, 17, 0, 23)
        self.repeat_password.setFixedSize(448, 106)
        self.repeat_password.set_password_mode()
        #  noinspection PyUnresolvedReferences
        self.main_layout.addWidget(self.repeat_password, alignment=Qt.AlignHCenter)

        self.error_label = QLabel(Translator.translate('Labels.UnableToLogin'))
        self.error_label.setStyleSheet("""
            QLabel {
                font-family: Outfit;
                color: #AA4A44;
                font-size: 15px;
            }
        """)
        self.error_label.setFixedSize(431, 57)
        self.error_label.setContentsMargins(0, 0, 0, 23)
        self.error_label.setVisible(False)
        # noinspection PyUnresolvedReferences
        self.main_layout.addWidget(self.error_label, alignment=Qt.AlignHCenter)

        btn_register = ButtonBasic(Translator.translate('Buttons.Register'))
        btn_register.clicked.connect(self.controller.register)
        btn_register.setFixedSize(394, 60)
        btn_register.setContentsMargins(0, 20, 0, 38)
        # noinspection PyUnresolvedReferences
        self.main_layout.addWidget(btn_register, alignment=Qt.AlignHCenter)
        enter_for_login = QShortcut(QKeySequence("Return"), self)
        enter_for_login.activated.connect(self.controller.register)
        self.main_layout.addStretch()

    def get_name(self) -> str:
        return self.input_name.get_text()

    def get_last_name(self) -> str:
        return self.input_last_name.get_text()

    def get_mail(self) -> str:
        return self.input_mail.get_text()

    def get_password(self) -> str:
        return self.input_password.get_text()

    def get_repeat_password(self) -> str:
        return self.repeat_password.get_text()

    def set_valid_name(self, is_valid: bool):
        self.input_name.set_valid_style(is_valid)

    def set_valid_last_name(self, is_valid: bool):
        self.input_last_name.set_valid_style(is_valid)

    def set_valid_password(self, is_valid: bool):
        self.input_password.set_valid_style(is_valid)
        self.repeat_password.set_valid_style(is_valid)

    def set_valid_mail(self, is_valid: bool):
        self.input_mail.set_valid_style(is_valid)

    def set_valid_label(self, is_valid: bool, error_message: str = ''):
        self.error_label.setVisible(not is_valid)
        self.error_label.setText(error_message)

    def show_error(self, error):
        # noinspection PyArgumentList
        QMessageBox.critical(self, Translator.translate('WindowTitles.Error'), str(error))
