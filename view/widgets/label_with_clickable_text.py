from typing import Callable

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QWidget, QHBoxLayout


class LabelWithClickableText(QWidget):
    def __init__(self, base_text: str, clickable_text: str, foo_to_call: Callable, parent=None):
        super().__init__(parent)
        self.base_text = base_text
        self.clickable_text = clickable_text
        self.foo_to_call = foo_to_call
        self.main_layout = QHBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.setLayout(self.main_layout)
        self.label = QLabel(base_text)
        self.label.setContentsMargins(0, 0, 5, 0)
        self.main_layout.addWidget(self.label)
        self.clickable_label = ClickableLabel(clickable_text, self.foo_to_call)
        self.main_layout.addWidget(self.clickable_label)

    def set_base_text_style(self, style: str):
        self.label.setStyleSheet(style)

    def set_clickable_text_style(self, style: str):
        self.clickable_label.setStyleSheet(style)

class ClickableLabel(QLabel):
    def __init__(self, text, function_to_call, parent=None):
        super().__init__(parent)
        # noinspection PyUnresolvedReferences
        self.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.setOpenExternalLinks(False)
        self.function_to_call = function_to_call
        self.linkActivated.connect(self.function_to_call)
        self.setText(
            f'<a href="clickable" style="text-decoration: none; color: #3A4D39;">{text}</a>'
        )
