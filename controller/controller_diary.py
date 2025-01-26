from __future__ import annotations

from typing import TYPE_CHECKING

from models.diary_entry import DiaryEntry
from utils.db_connection import DBConnection
from utils.exceptions.db_unable_to_get_data import DBUnableToGetData
from utils.user_session import UserSession

if TYPE_CHECKING:
    from view.screen_diary import ScreenDiary


class ControllerDiary:
    def __init__(self, view: ScreenDiary):
        """
        :raise DBUnableToGetData
        """
        self._view = view
        self._db = DBConnection()
        self._diary_entries = self._get_diary_entries_from_db()

    def get_diary_entries(self):
        return self._diary_entries

    def refresh_diary_entries(self):
        """
        :raise DBUnableToGetData
        """
        self._diary_entries = self._get_diary_entries_from_db()

    def _get_diary_entries_from_db(self):
        """
        :raise DBUnableToGetData
        """
        data = self._db.get_diary_entries(UserSession().user_id)
        try:
            return list(map(DiaryEntry, data.data))
        except Exception:
            raise DBUnableToGetData()
