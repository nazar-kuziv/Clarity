from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QSizePolicy, \
    QMessageBox, QCheckBox

from controller.controller_share import ControllerShare
from utils.environment import Environment
from utils.i18n import Translator
from view.widgets.button_basic import ButtonBasic
from view.widgets.input_validated_label import InputValidatedLabel


class ScreenShare(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._controller = ControllerShare(self)
        space_layout = QVBoxLayout(self)
        # noinspection PyUnresolvedReferences
        space_layout.setAlignment(Qt.AlignCenter)
        space_layout.setContentsMargins(0, 0, 0, 0)
        space_layout.setSpacing(0)
        main_widget = QWidget()
        main_widget.setContentsMargins(0, 0, 0, 0)
        main_widget.setMaximumSize(700, 900)
        # noinspection PyUnresolvedReferences
        space_layout.addWidget(main_widget)
        # noinspection PyUnresolvedReferences
        main_widget.setAttribute(Qt.WA_StyledBackground, True)
        main_widget.setObjectName('main_widget')
        main_widget.setStyleSheet("""
            #main_widget {
                background-color: #739072;
                border-radius: 10px;
                margin-bottom: 150px;
            }
        """)
        main_widget.setFixedSize(950, 750)
        self._main_layout = QVBoxLayout(main_widget)
        main_widget.setLayout(self._main_layout)
        close_layout = QHBoxLayout()
        self._main_layout.addLayout(close_layout)
        close_layout.addStretch()
        close_btn = QPushButton()
        close_btn.setFixedSize(50, 50)
        close_btn.setIconSize(QSize(50, 50))
        close_btn.setIcon(QPixmap(Environment.resource_path('static/images/close.png')))
        # noinspection PyUnresolvedReferences
        close_layout.addWidget(close_btn, alignment=Qt.AlignRight)
        close_btn.setStyleSheet("""
            QPushButton {
                border: none;
                background-color: transparent;
                padding: 0;
                outline: none;
            }

            QPushButton:hover {
                background-color: rgba(0, 0, 0, 40);  
                border-radius: 10px; 
            }

            QPushButton:pressed {
                background-color: rgba(0, 0, 0, 60);  
                border-radius: 10px;
            }
        """)
        close_btn.clicked.connect(self.deleteLater)
        share_your_diary_label = QLabel(Translator.translate('Labels.ShareYourDiary'))
        share_your_diary_label.setStyleSheet("""
                   QLabel {
                       font-family: Outfit;
                       font-weight: bold;
                       color: #FFF8EB;
                       font-size: 52px;
                   }
               """)
        # noinspection PyUnresolvedReferences
        share_your_diary_label.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        # noinspection PyUnresolvedReferences
        self._main_layout.addWidget(share_your_diary_label, alignment=Qt.AlignTop | Qt.AlignHCenter)

        self._input_mail = InputValidatedLabel(Translator.translate('Labels.InputEmailForShare'), parent=main_widget)
        self._input_mail.setContentsMargins(0, 17, 0, 0)
        self._input_mail.setFixedSize(580, 100)
        self._input_mail.set_label_text_style("""
            QLabel {
                font-family: Outfit;
                color: #FFF8EB;
                font-size: 20px;
            }
        """)
        # noinspection PyUnresolvedReferences
        self._main_layout.addWidget(self._input_mail, alignment=Qt.AlignHCenter)

        self._start_date = InputValidatedLabel(Translator.translate('Labels.StartDate'), parent=main_widget)
        self._start_date.setContentsMargins(0, 17, 0, 0)
        self._start_date.setFixedSize(580, 100)
        self._start_date.set_label_text_style("""
        	QLabel {
        		font-family: Outfit;
        		color: #FFF8EB;
        		font-size: 20px;
        	}
        """)
        self._start_date.set_placeholder('YYYY-MM-DD')
        # noinspection PyUnresolvedReferences
        self._main_layout.addWidget(self._start_date, alignment=Qt.AlignHCenter)

        self._end_date = InputValidatedLabel(Translator.translate('Labels.EndDate'), parent=main_widget)
        self._end_date.setContentsMargins(0, 17, 0, 0)
        self._end_date.setFixedSize(580, 100)
        self._end_date.set_label_text_style("""
        	QLabel {
        		font-family: Outfit;
        		color: #FFF8EB;
        		font-size: 20px;
        	}
        """)
        self._end_date.set_placeholder('YYYY-MM-DD')
        # noinspection PyUnresolvedReferences
        self._main_layout.addWidget(self._end_date, alignment=Qt.AlignHCenter)

        checkbox_root_widget = QWidget()
        checkbox_layout = QHBoxLayout()
        checkbox_layout.setContentsMargins(0, 0, 0, 0)
        checkbox_layout.setSpacing(0)
        checkbox_root_widget.setLayout(checkbox_layout)
        checkbox_root_widget.setContentsMargins(0, 0, 0, 0)
        checkbox_root_widget.setFixedSize(580, 60)
        label_share_without_content = QLabel(Translator.translate('Labels.ShareWithoutContent'))
        label_share_without_content.setContentsMargins(0, 0, 0, 0)
        label_share_without_content.setStyleSheet("""
        	QLabel {
        		font-family: Outfit;
        		color: #FFF8EB;
        		font-size: 20px;
        	}
        """)
        checkbox_layout.addWidget(label_share_without_content)
        self._checkbox_share_without_content = QCheckBox()
        self._checkbox_share_without_content.setContentsMargins(0, 0, 0, 0)
        self._checkbox_share_without_content.setStyleSheet("margin-left: 10px;")
        checkbox_layout.addWidget(self._checkbox_share_without_content)
        checkbox_layout.addStretch()
        # noinspection PyUnresolvedReferences
        self._main_layout.addWidget(checkbox_root_widget, alignment=Qt.AlignHCenter)

        btn_login = ButtonBasic(Translator.translate('Buttons.Share'))
        btn_login.clicked.connect(self._controller.send_diary_entries)
        btn_login.setFixedSize(394, 60)
        btn_login.setContentsMargins(0, 0, 0, 45)
        # noinspection PyUnresolvedReferences
        self._main_layout.addWidget(btn_login, alignment=Qt.AlignHCenter)

        self._main_layout.addStretch()

    def get_email(self) -> str:
        return self._input_mail.get_text()

    def set_valid_mail(self, is_valid: bool):
        self._input_mail.set_valid_style(is_valid)

    def get_start_date(self) -> str:
        return self._start_date.get_text()

    def set_valid_start_date(self, is_valid: bool):
        self._start_date.set_valid_style(is_valid)

    def get_end_date(self) -> str:
        return self._end_date.get_text()

    def set_valid_end_date(self, is_valid: bool):
        self._end_date.set_valid_style(is_valid)

    def is_share_without_content(self) -> bool:
        return self._checkbox_share_without_content.isChecked()

    def show_error(self, error):
        # noinspection PyArgumentList
        QMessageBox.critical(self, Translator.translate('WindowTitles.Error'), str(error))
