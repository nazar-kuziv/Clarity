from functools import partial

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QScrollArea, QGridLayout, QMessageBox, QStackedLayout

from controller.controller_diary import ControllerDiary
from utils.i18n import Translator
from view.widgets.widget_diary_entry import WidgetDiaryEntry


class ScreenDiary(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        try:
            self._controller_diary = ControllerDiary(self)
        except Exception as e:
            self.show_error(str(e))
            return

        # noinspection PyUnresolvedReferences
        self.setAttribute(Qt.WA_StyledBackground, True)

        self._main_layout = QStackedLayout(self)
        # noinspection PyUnresolvedReferences
        self._main_layout.setStackingMode(QStackedLayout.StackAll)

        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setSpacing(0)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        # noinspection PyUnresolvedReferences
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # noinspection PyUnresolvedReferences
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        content_widget = QWidget()
        content_widget.setObjectName('content_widget')
        content_widget.setStyleSheet("""
            #content_widget {
                background-color: #FFF8EA;
            }
        """)
        self._content_layout = QGridLayout(content_widget)
        self._content_layout.setContentsMargins(0, 0, 0, 0)
        self._content_layout.setSpacing(0)
        self._content_layout.setHorizontalSpacing(10)
        self._content_layout.setVerticalSpacing(20)
        scroll_area.setWidget(content_widget)

        self._main_layout.addWidget(scroll_area)

        self._show_diary_entries()

    def _show_diary_entries(self):
        diary_entries = self._controller_diary.get_diary_entries()
        for i in range(0, len(diary_entries), 2):
            new_widget = WidgetDiaryEntry(str(diary_entries[i].creation_date), diary_entries[i].entry_text)
            new_widget.clicked.connect(
                partial(lambda j: print(f'Diary entry clicked {str(diary_entries[j].creation_date)}'), i))
            self._content_layout.addWidget(new_widget, i, 0)
            if i + 1 < len(diary_entries):
                new_widget = WidgetDiaryEntry(str(diary_entries[i + 1].creation_date), diary_entries[i + 1].entry_text)
                new_widget.clicked.connect(
                    partial(lambda j: print(f'Diary entry clicked {str(diary_entries[j + 1].creation_date)}'), i))
                self._content_layout.addWidget(new_widget, i, 1)

    def show_error(self, message):
        # noinspection PyArgumentList
        QMessageBox.critical(self, Translator.translate('WindowTitles.Error'), str(message))
