from __future__ import annotations

from typing import TYPE_CHECKING

from models.diary_entry import DiaryEntry
from utils.db_connection import DBConnection
from utils.exceptions.db_unable_to_get_data import DBUnableToGetData
from utils.user_session import UserSession

if TYPE_CHECKING:
    from view.screen_share import ScreenShare


class ControllerShare:
    def __init__(self, view: ScreenShare):
        self._view = view
        self._db = DBConnection()

    def get_diary_entries_for_time_period(self, start_date: str, end_date: str) -> list[DiaryEntry]:
        try:
            user_id = UserSession().user_id
            data = self._db.get_diary_entries_for_time_period(user_id, start_date, end_date)
            return list(map(DiaryEntry, data.data))
        except Exception:
            raise DBUnableToGetData()
