from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QTextEdit, QSizePolicy, \
    QMessageBox

from controller.controller_diary_entry import ControllerDiaryEntry
from models.diary_entry import DiaryEntry
from utils.environment import Environment
from utils.i18n import Translator


class ScreenDiaryEntry(QWidget):
    def __init__(self, diary_entry: DiaryEntry = None, parent=None):
        super().__init__(parent)
        self._controller = ControllerDiaryEntry(self, diary_entry)
        space_layout = QVBoxLayout(self)
        # noinspection PyUnresolvedReferences
        space_layout.setAlignment(Qt.AlignCenter)
        space_layout.setContentsMargins(0, 0, 0, 0)
        space_layout.setSpacing(0)
        main_widget = QWidget()
        main_widget.setContentsMargins(0, 0, 0, 0)
        main_widget.setMaximumWidth(950)
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
        date_save_close_layout = QHBoxLayout()
        self._main_layout.addLayout(date_save_close_layout)
        date_label = QLabel(self._controller.get_creation_date())
        # noinspection PyUnresolvedReferences
        date_save_close_layout.addWidget(date_label, alignment=Qt.AlignLeft)
        date_label.setStyleSheet("""
            QLabel {
                color: #FFFFFF;
                font-family: Outfit;
                font-size: 20px;
                font-weight: bold;
            }
        """)
        date_save_close_layout.addStretch()
        self._save_btn = QPushButton()
        self._save_btn.setFixedSize(50, 50)
        self._save_btn.setIconSize(QSize(50, 50))
        self._save_btn.setIcon(QPixmap(Environment.resource_path('static/images/save.png')))
        self._save_btn.clicked.connect(self._controller.save_diary_entry_close_view)
        # noinspection PyUnresolvedReferences
        date_save_close_layout.addWidget(self._save_btn, alignment=Qt.AlignRight)
        self._save_btn.setStyleSheet("""
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
        self._save_btn.setVisible(False)
        close_btn = QPushButton()
        close_btn.setFixedSize(50, 50)
        close_btn.setIconSize(QSize(50, 50))
        close_btn.setIcon(QPixmap(Environment.resource_path('static/images/close.png')))
        # noinspection PyUnresolvedReferences
        date_save_close_layout.addWidget(close_btn, alignment=Qt.AlignRight)
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
        self._entry_text_input = QTextEdit(self._controller.get_text())
        # noinspection PyUnresolvedReferences
        self._entry_text_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self._entry_text_input.setStyleSheet("""
            QTextEdit {
                color: #FFFFFF;
                font-family: Outfit;
                font-size: 25px;
                font-weight: bold;
                background-color: transparent;
                border: 1px solid #FFFFFF;
                margin-bottom: 150px;
            }
        """)
        self._entry_text_input.textChanged.connect(self._change_visibility_of_save_btn)
        self._main_layout.addWidget(self._entry_text_input)

    def _change_visibility_of_save_btn(self):
        if self._controller.has_been_text_modified(self._entry_text_input.toPlainText()):
            self._save_btn.setVisible(True)
        else:
            self._save_btn.setVisible(False)

    def get_entry_text(self):
        return self._entry_text_input.toPlainText()

    def show_error(self, error):
        # noinspection PyArgumentList
        QMessageBox.critical(self, Translator.translate('WindowTitles.Error'), str(error))
