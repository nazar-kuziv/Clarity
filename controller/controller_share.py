from __future__ import annotations

import re
from datetime import datetime
from typing import TYPE_CHECKING

from models.diary_entry import DiaryEntry
from utils.db_connection import DBConnection
from utils.environment import Environment
from utils.exceptions.db_unable_to_get_data import DBUnableToGetData
from utils.exceptions.heatmap_export_failed import HeatmapExportFailed
from utils.exceptions.mail_unable_to_send import MailUnableToSend
from utils.exceptions.xlsx_export_failed import XlsxExportFailed
from utils.i18n import Translator
from utils.mail import MailService
from utils.user_session import UserSession

if TYPE_CHECKING:
    from view.screen_share import ScreenShare


class ControllerShare:
    def __init__(self, view: ScreenShare):
        self._view = view
        self._db = DBConnection()
        self.mail_service = MailService()

    def _get_diary_entries_for_time_period(self, start_date: str, end_date: str) -> list[DiaryEntry]:
        try:
            user_id = UserSession().user_id
            data = self._db.get_diary_entries_for_time_period(user_id, start_date, end_date)
            return list(map(DiaryEntry, data.data))
        except Exception:
            raise DBUnableToGetData()

    def send_diary_entries(self):
        email = self._view.get_email()
        if not self._is_mail_valid(email):
            self._view.set_valid_mail(False)
            return
        self._view.set_valid_mail(True)
        start_date = self._view.get_start_date()
        if not self._is_date_valid(start_date):
            self._view.set_valid_start_date(False)
            return
        self._view.set_valid_start_date(True)
        end_date = self._view.get_end_date()
        if not self._is_date_valid(end_date):
            self._view.set_valid_end_date(False)
            return
        self._view.set_valid_end_date(True)
        dt_start_date = datetime.strptime(start_date, "%Y-%m-%d")
        dt_end_date = datetime.strptime(end_date, "%Y-%m-%d")
        if dt_start_date.date() > dt_end_date.date():
            self._view.set_valid_start_date(False)
            self._view.set_valid_end_date(False)
            return
        try:
            diary_entries = self._get_diary_entries_for_time_period(start_date, end_date)
            file_name = f"diary_entries_{datetime.now().strftime('%Y-%m-%d_%H-%M')}"
            xlsx_file_path = Environment.resource_path(f"tmp/{file_name}.xlsx")
            DiaryEntry.export_list_to_xlsx(diary_entries, xlsx_file_path, self._view.is_share_without_content())
            files = [xlsx_file_path]
            usr = UserSession()
            visibility = Translator.translate(
                'Mail.WithoutContent') if self._view.is_share_without_content() else Translator.translate(
                'Mail.WithContent')
            png_file_path = Environment.resource_path(f"tmp/{file_name}.png")
            files.extend(DiaryEntry.export_list_to_heatmap(diary_entries, dt_start_date, dt_end_date, png_file_path))
            self.mail_service.send_mail_with_attachments(
                to_email=email,
                subject=Translator.translate('Mail.Subject').format(name=usr.name, last_name=usr.last_name),
                body=Translator.translate('Mail.Body').format(name=usr.name, last_name=usr.last_name,
                                                              visibility=visibility, start_date=start_date,
                                                              end_date=end_date),
                attachments=files
            )
        except DBUnableToGetData as db_error:
            self._view.show_error(str(db_error))
            return
        except XlsxExportFailed as xls_error:
            self._view.show_error(str(xls_error))
            return
        except HeatmapExportFailed as heatmap_error:
            self._view.show_error(str(heatmap_error))
            return
        except MailUnableToSend as mail_error:
            self._view.show_error(str(mail_error))
            return
        except Exception:
            self._view.show_error(Translator.translate('Errors.SomethingWentWrong'))
            return
        self._view.deleteLater()

    @staticmethod
    def _is_mail_valid(email: str) -> bool:
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None

    @staticmethod
    def _is_date_valid(date: str) -> bool:
        try:
            datetime.strptime(date, "%Y-%m-%d")
            if date > datetime.now().strftime("%Y-%m-%d"):
                return False
            return True
        except ValueError:
            return False
