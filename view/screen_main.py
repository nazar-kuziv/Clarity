from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QStackedLayout, QSizePolicy

from utils.environment import Environment


class ScreenMain(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # noinspection PyUnresolvedReferences
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('background-color: #FFF8EA;')
        self._main_layout = QVBoxLayout()
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setSpacing(0)
        self.setLayout(self._main_layout)

        self._butons_widget = QWidget()
        self._butons_widget.setContentsMargins(0, 20, 0, 0)
        butons_layout = QHBoxLayout(self._butons_widget)
        self._main_layout.addWidget(self._butons_widget)
        butons_layout.setContentsMargins(0, 0, 0, 0)
        butons_layout.setSpacing(0)
        # noinspection PyUnresolvedReferences
        butons_layout.setAlignment(Qt.AlignRight)

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
        butons_layout.addWidget(self._share_btn)

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
        butons_layout.addWidget(self._stats_btn)

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
        butons_layout.addWidget(self._filter_btn)

        central_widget = QWidget()
        # noinspection PyUnresolvedReferences
        central_widget.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self._central_widget_layout = QStackedLayout(central_widget)
        self._central_widget_layout.setContentsMargins(0, 0, 0, 0)
        self._central_widget_layout.setSpacing(0)
        # noinspection PyUnresolvedReferences
        self._central_widget_layout.setStackingMode(QStackedLayout.StackAll)
        self._main_layout.addWidget(central_widget)

    def _disable_buttons(self):
        self._share_btn.setDisabled(True)
        self._stats_btn.setDisabled(True)
        self._filter_btn.setDisabled(True)
