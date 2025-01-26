from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedLayout, QSizePolicy, \
    QGraphicsOpacityEffect, QMessageBox

from utils.environment import Environment
from utils.i18n import Translator
from view.screen_diary import ScreenDiary
from view.screen_diary_entry import ScreenDiaryEntry


class ScreenMain(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(1024, 576)
        # noinspection PyUnresolvedReferences
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowTitle(Translator.translate('WindowTitles.MyDiary'))
        self.setObjectName('main_screen')
        self.setStyleSheet("""
            #main_screen {
                background-color: #FFF8EA;
            }
        """)
        self._main_layout = QVBoxLayout()
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setSpacing(0)
        self.setLayout(self._main_layout)

        self._butons_widget = QWidget()
        self._butons_widget.setContentsMargins(0, 20, 0, 0)
        buttons_layout = QVBoxLayout(self._butons_widget)
        small_butons_layout = QHBoxLayout()
        buttons_layout.addLayout(small_butons_layout)
        self._main_layout.addWidget(self._butons_widget)
        small_butons_layout.setContentsMargins(0, 0, 0, 0)
        small_butons_layout.setSpacing(0)
        # noinspection PyUnresolvedReferences
        small_butons_layout.setAlignment(Qt.AlignRight)

        self._share_btn = QPushButton()
        self._share_btn.setIcon(QIcon(Environment.resource_path('static/images/share.png')))
        self._share_btn.setFixedSize(67, 50)
        self._share_btn.setIconSize(QSize(30, 30))
        self._share_btn.setStyleSheet("""
        	QPushButton {
        		background-color: #ECE3CE;
        		border-radius: 25px;
        		margin-right: 17px;
        		border: 1px solid #D4C69F;
        	}

        	QPushButton:hover {
        		background-color: #F2E1A1;  
        	}

        	QPushButton:pressed {
        		background-color: #D4C69F;  
        	}
        """)
        self._share_btn.clicked.connect(lambda x: print('Share button clicked'))
        small_butons_layout.addWidget(self._share_btn)

        self._stats_btn = QPushButton()
        self._stats_btn.setIcon(QIcon(Environment.resource_path('static/images/analysis.png')))
        self._stats_btn.setFixedSize(67, 50)
        self._stats_btn.setIconSize(QSize(30, 30))
        self._stats_btn.setStyleSheet("""
        	QPushButton {
        		background-color: #ECE3CE;
        		border-radius: 25px;
        		margin-right: 17px;
        		border: 1px solid #D4C69F;
        	}

        	QPushButton:hover {
        		background-color: #F2E1A1;  
        	}

        	QPushButton:pressed {
        		background-color: #D4C69F;  
        	}
        """)
        self._stats_btn.clicked.connect(lambda x: print('Stats button clicked'))
        small_butons_layout.addWidget(self._stats_btn)

        self._filter_btn = QPushButton()
        self._filter_btn.setIcon(QIcon(Environment.resource_path('static/images/filter.png')))
        self._filter_btn.setFixedSize(78, 50)
        self._filter_btn.setIconSize(QSize(30, 30))
        self._filter_btn.setStyleSheet("""
            QPushButton {
                background-color: #ECE3CE;
                border-radius: 25px;
                margin-right: 28px;
                border: 1px solid #D4C69F;
            }

            QPushButton:hover {
                background-color: #F2E1A1;  
            }

            QPushButton:pressed {
                background-color: #D4C69F;  
            }
        """)
        self._filter_btn.clicked.connect(lambda x: print('Filter button clicked'))
        small_butons_layout.addWidget(self._filter_btn)

        self._add_entry_btn = QPushButton(f"   {Translator.translate('Buttons.AddEntry')}")
        self._add_entry_btn.setIcon(QIcon(Environment.resource_path('static/images/edit.png')))
        self._add_entry_btn.setIconSize(QSize(35, 35))
        self._add_entry_btn.setMinimumHeight(125)
        self._add_entry_btn.setStyleSheet("""
            QPushButton {
                font-family: Outfit;
                font-size: 24px;
                font-weight: bold;
                background-color: rgba(158, 118, 118, 0.8); 
                color: #FFFFFF;
                border-radius: 20px;
                margin: 25px 220px 60px 220px;
            }
            QPushButton:hover {
                background-color: #9E7676; 
            }
            QPushButton:pressed {
                background-color: #815B5B; 
            }
        """)
        self._add_entry_btn.clicked.connect(self._show_diary_entry_screen)
        buttons_layout.addWidget(self._add_entry_btn)

        central_widget = QWidget()
        # noinspection PyUnresolvedReferences
        central_widget.setAttribute(Qt.WA_StyledBackground, True)
        central_widget.setObjectName('central_widget')
        central_widget.setStyleSheet("""
            #central_widget {
                background-color: #FFF8EA;
            }
        """)
        # noinspection PyUnresolvedReferences
        central_widget.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self._central_widget_layout = QStackedLayout(central_widget)
        self._central_widget_layout.setContentsMargins(0, 0, 0, 0)
        self._central_widget_layout.setSpacing(0)
        # noinspection PyUnresolvedReferences
        self._central_widget_layout.setStackingMode(QStackedLayout.StackAll)
        self._main_layout.addWidget(central_widget)

        self._diary_screen = ScreenDiary(self)
        self._diary_screen.top_widget_changed.connect(
            lambda x: self._change_buttons_state_with_blur(self._share_btn.isEnabled()))
        self._central_widget_layout.addWidget(self._diary_screen)

    def _show_diary_entry_screen(self):
        self._change_buttons_state_with_blur(self._share_btn.isEnabled())
        self._diary_screen.change_previews_diary_entries_state_with_blur(True)
        self._screen_diary_entry = ScreenDiaryEntry()
        # noinspection PyUnresolvedReferences
        self._screen_diary_entry.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self._screen_diary_entry.destroyed.connect(self._change_current_widget_reload_diaries_previews)
        diary_entry_screen_index = self._central_widget_layout.addWidget(self._screen_diary_entry)
        self._central_widget_layout.setCurrentIndex(diary_entry_screen_index)

    def _change_current_widget_reload_diaries_previews(self):
        self._change_buttons_state_with_blur(self._share_btn.isEnabled())
        self._diary_screen.change_previews_diary_entries_state_with_blur(False)
        try:
            self._diary_screen.reload_diaries_previews()
        except Exception as e:
            self.show_error(str(e))

    def _change_buttons_state_with_blur(self, disable: bool):
        self._share_btn.setDisabled(disable)
        self._stats_btn.setDisabled(disable)
        self._filter_btn.setDisabled(disable)
        self._add_entry_btn.setDisabled(disable)

        if disable:
            opacity_effect = QGraphicsOpacityEffect(self._butons_widget)
            opacity_effect.setOpacity(0.1)
            self._butons_widget.setGraphicsEffect(opacity_effect)
        else:
            # noinspection PyTypeChecker
            self._butons_widget.setGraphicsEffect(None)

    def show_error(self, message):
        # noinspection PyArgumentList
        QMessageBox.critical(self, Translator.translate('WindowTitles.Error'), str(message))
