from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from models.diary_entry import DiaryEntry
from utils.db_connection import DBConnection
from utils.sentiment import Sentiment
from utils.user_session import UserSession

if TYPE_CHECKING:
    from view.screen_diary_entry import ScreenDiaryEntry


class ControllerDiaryEntry:
    def __init__(self, view: ScreenDiaryEntry, diary_entry: DiaryEntry = None):
        self._view = view
        self._diary_entry = diary_entry
        self._db = DBConnection()
        self._sentiment = Sentiment()
        self._creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def save_diary_entry_close_view(self):
        entry_text = self._view.get_entry_text()
        try:
            if self._diary_entry:
                self._db.alter_db_diary_entry(self._diary_entry.id, entry_text.strip(),
                                              self._sentiment.get_sentiment(entry_text))
            else:
                self._db.add_new_diary_entry(UserSession().user_id, entry_text.strip(),
                                             self._sentiment.get_sentiment(entry_text),
                                             self._creation_date)
            self._view.deleteLater()
        except Exception as e:
            self._view.show_error(str(e))


    def get_creation_date(self):
        if self._diary_entry:
            return str(self._diary_entry.creation_date)
        else:
            return self._creation_date

    def get_text(self):
        if self._diary_entry:
            return self._diary_entry.entry_text
        else:
            return ""

    def has_been_text_modified(self, view_text: str):
        if not view_text or not view_text.strip():
            return False
        if self._diary_entry:
            return view_text.strip() != self._diary_entry.entry_text
        return True
