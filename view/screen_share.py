from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QSizePolicy, \
    QMessageBox

from controller.controller_share import ControllerShare
from utils.environment import Environment
from utils.i18n import Translator
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
        main_widget.setFixedSize(700, 900)
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
                       margin-top: 32px;
                   }
               """)
        # noinspection PyUnresolvedReferences
        share_your_diary_label.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        # noinspection PyUnresolvedReferences
        self._main_layout.addWidget(share_your_diary_label, alignment=Qt.AlignTop | Qt.AlignHCenter)

        self._input_mail = InputValidatedLabel(Translator.translate('Labels.InputEmailForShare'), parent=main_widget)
        self._input_mail.setContentsMargins(0, 17, 0, 0)
        self._input_mail.setFixedSize(580, 100)
        # noinspection PyUnresolvedReferences
        self._main_layout.addWidget(self._input_mail, alignment=Qt.AlignHCenter)

        self._main_layout.addStretch()

    def set_valid_mail(self, is_valid: bool):
        self._input_mail.set_valid_style(is_valid)

    def show_error(self, error):
        # noinspection PyArgumentList
        QMessageBox.critical(self, Translator.translate('WindowTitles.Error'), str(error))
