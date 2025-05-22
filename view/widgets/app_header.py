from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QSizePolicy

from utils.environment import Environment
from utils.i18n import Translator


class AppHeader(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setContentsMargins(0, 0, 0, 0)
        # noinspection PyUnresolvedReferences
        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        app_name = QLabel(Translator.translate('Labels.Clarity'))
        app_name.setStyleSheet("""
            QLabel {
                font-family: Junge;
                font-size: 44px;
                color: #000000;
            }   
        """)
        main_layout.addWidget(app_name)
        logo_label = QLabel()
        logo_pixmap = QPixmap(Environment.resource_path('static/images/logo.png'))
        logo_label.setPixmap(logo_pixmap.scaled(91, 91))
        main_layout.addWidget(logo_label)
