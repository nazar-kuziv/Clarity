from __future__ import annotations

import re
from typing import TYPE_CHECKING

import bcrypt

from utils.db_connection import DBConnection
from utils.exceptions.db_unable_to_get_data import DBUnableToGetData
from utils.i18n import Translator
from utils.user_session import UserSession

if TYPE_CHECKING:
    from view.screen_login import ScreenLogin


class ControllerLogin:
    def __init__(self, view: ScreenLogin, after_login_callback=None):
        self._view = view
        self._after_login_callback = after_login_callback
        self._db = DBConnection()

    def login(self):
        try:
            if not self._is_valid_mail(self._view.get_mail()):
                self._view.set_valid_mail(False)
                self._view.set_valid_label(False)
                return
            if self._login_user(self._view.get_mail(), self._view.get_password()):
                self._after_login_callback()
            else:
                self._view.set_valid_mail(False)
                self._view.set_valid_password(False)
                self._view.set_valid_label(False)
        except DBUnableToGetData as e:
            self._view.show_error(str(e))
        except Exception:
            self._view.show_error(Translator.translate('Errors.SomethingWentWrong'))

    @staticmethod
    def _is_valid_mail(mail: str) -> bool:
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(email_regex, mail))

    def _login_user(self, mail: str, password: str):
        db_user = self._db.get_user(mail.lower()).data
        if len(db_user) == 0 or not db_user[0]['password'] or not self._verify_password(
                db_user[0]['password'], password):
            return False
        user_session = UserSession()
        user_session.set_user_data(db_user[0]['user_id'], db_user[0]['email'], db_user[0]['name'],
                                   db_user[0]['last_name'])
        return True

    @staticmethod
    def _verify_password(password_hash: str, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))
