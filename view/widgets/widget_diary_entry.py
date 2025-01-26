from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class WidgetDiaryEntry(QWidget):
    clicked = Signal()

    def __init__(self, date: str, text: str, parent=None):
        super().__init__(parent)
        self.setContentsMargins(0, 0, 0, 0)
        self.setMaximumWidth(570)
        self._main_layout = QVBoxLayout(self)
        self._main_layout.setSpacing(0)

        # noinspection PyUnresolvedReferences
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setObjectName("diary_entry")
        self.setStyleSheet("""
            #diary_entry {
                background-color: #739072;
                border-radius: 10px;
            }
            #diary_entry:hover {
                background-color: #8b9f86;
                border-radius: 10px;
            }
        """)

        date_label = QLabel(date)
        date_label.setStyleSheet("""
            QLabel {
                color: #FFFFFF;
                font-family: Outfit;
                font-size: 14px;
                font-weight: bold;            
            }
        """)
        # noinspection PyUnresolvedReferences
        self._main_layout.addWidget(date_label, alignment=Qt.AlignLeft)

        self._main_layout.addSpacing(150)

        text_label = QLabel(text if len(text) < 171 else text[:168] + '...')
        text_label.setWordWrap(True)
        text_label.setStyleSheet("""
            QLabel {
                color: #FFFFFF;
                font-family: Outfit;
                font-weight: bold;
                font-size: 20px;
            }
        """)
        # noinspection PyUnresolvedReferences
        self._main_layout.addWidget(text_label, alignment=Qt.AlignBottom)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.setStyleSheet("background-color: #557b5f;border-radius: 10px;")
        self.clicked.emit()

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        self.setStyleSheet("""
                    #diary_entry {
                        background-color: #739072;
                        border-radius: 10px;
                    }
                    #diary_entry:hover {
                        background-color: #8b9f86;
                        border-radius: 10px;
                    }
        """)
