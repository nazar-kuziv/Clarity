from functools import partial

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QScrollArea, QGridLayout, QMessageBox, QStackedLayout, QGraphicsOpacityEffect, \
    QSizePolicy

from controller.controller_diary import ControllerDiary
from models.diary_entry import DiaryEntry
from utils.exceptions.db_unable_to_get_data import DBUnableToGetData
from utils.i18n import Translator
from view.screen_diary_entry import ScreenDiaryEntry
from view.widgets.preview_diary_entry import PreviewDiaryEntry


class ScreenDiary(QWidget):
    top_widget_changed = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)

        try:
            self._controller = ControllerDiary(self)
        except Exception as e:
            self.show_error(str(e))
            return

        # noinspection PyUnresolvedReferences
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setObjectName('diary_screen')
        self.setStyleSheet("""
            #diary_screen {
                background-color: #FFF8EA;
            }
        """)

        self._main_layout = QStackedLayout(self)
        # noinspection PyUnresolvedReferences
        self._main_layout.setStackingMode(QStackedLayout.StackAll)

        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setSpacing(0)

        scroll_area = QScrollArea()
        # noinspection PyUnresolvedReferences
        scroll_area.setFrameShape(QScrollArea.NoFrame)
        scroll_area.setAutoFillBackground(False)
        scroll_area.viewport().setAutoFillBackground(False)
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("background: transparent; border: none;")

        # noinspection PyUnresolvedReferences
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # noinspection PyUnresolvedReferences
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self._content_widget = QWidget()
        self._content_widget.setAutoFillBackground(False)
        self._content_layout = QGridLayout(self._content_widget)
        self._content_layout.setContentsMargins(0, 0, 0, 0)
        self._content_layout.setSpacing(0)
        self._content_layout.setHorizontalSpacing(10)
        self._content_layout.setVerticalSpacing(20)
        scroll_area.setWidget(self._content_widget)

        self._main_layout.addWidget(scroll_area)
        self._main_layout.currentChanged.connect(self.top_widget_changed.emit)
        self._main_layout.currentChanged.connect(
            lambda: self.change_previews_diary_entries_state_with_blur(self._are_previews_diary_entries_enabled()))
        self._show_previews_diary_entries()

    def _show_previews_diary_entries(self):
        diary_entries = self._controller.get_diary_entries()
        for i in range(0, len(diary_entries), 2):
            new_widget = PreviewDiaryEntry(str(diary_entries[i].creation_date), diary_entries[i].entry_text)
            new_widget.clicked.connect(partial(self._show_diary_entry_screen, diary_entries[i]))
            self._content_layout.addWidget(new_widget, i, 0)
            if i + 1 < len(diary_entries):
                new_widget = PreviewDiaryEntry(str(diary_entries[i + 1].creation_date), diary_entries[i + 1].entry_text)
                new_widget.clicked.connect(partial(self._show_diary_entry_screen, diary_entries[i + 1]))
                self._content_layout.addWidget(new_widget, i, 1)

    def _are_previews_diary_entries_enabled(self):
        return self._content_layout.itemAt(0).widget().isEnabled()

    def change_previews_diary_entries_state_with_blur(self, disable: bool):
        for i in range(self._content_layout.count()):
            self._content_layout.itemAt(i).widget().setDisabled(disable)
        if disable:
            opacity_effect = QGraphicsOpacityEffect(self._content_widget)
            opacity_effect.setOpacity(0.1)
            self._content_widget.setGraphicsEffect(opacity_effect)
        else:
            # noinspection PyTypeChecker
            self._content_widget.setGraphicsEffect(None)

    def _show_diary_entry_screen(self, diary_entry: DiaryEntry):
        self.screen_diary_entry = ScreenDiaryEntry(diary_entry)
        # noinspection PyUnresolvedReferences
        self.screen_diary_entry.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.screen_diary_entry.destroyed.connect(self._change_current_widget_reload_diaries_previews)
        diary_entry_screen_index = self._main_layout.addWidget(self.screen_diary_entry)
        self._main_layout.setCurrentIndex(diary_entry_screen_index)

    def _change_current_widget_reload_diaries_previews(self):
        try:
            self._main_layout.setCurrentIndex(0)
            self.reload_diaries_previews()
        except DBUnableToGetData as e:
            self.show_error(str(e))
        except Exception:
            self.show_error(Translator.translate('Errors.SomethingWentWrong'))

    def reload_diaries_previews(self):
        """
        :raise DBUnableToGetData
        """
        try:
            self._controller.refresh_diary_entries()
            for i in range(self._content_layout.count()):
                item = self._content_layout.itemAt(i)
                if item is not None:
                    widget = item.widget()
                    if widget:
                        widget.deleteLater()
            self._show_previews_diary_entries()
        except Exception:
            raise DBUnableToGetData()

    def show_error(self, message):
        # noinspection PyArgumentList
        QMessageBox.critical(self, Translator.translate('WindowTitles.Error'), str(message))
