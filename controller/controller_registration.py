from __future__ import annotations

import re
from typing import TYPE_CHECKING

import bcrypt

from utils.db_connection import DBConnection
from utils.exceptions.db_unable_to_insert_data import DBUnableToInsertData
from utils.exceptions.db_user_with_this_email_exist import DBUserWithThisEmailExist
from utils.i18n import Translator

if TYPE_CHECKING:
    from view.screen_registration import ScreenRegistration


class ControllerRegistration:
    def __init__(self, view: ScreenRegistration, after_login_callback=None):
        self._view = view
        self._db = DBConnection()
        self._after_login_callback = after_login_callback

    def register(self):
        try:
            user_name = self._view.get_name()
            if not self._is_valid_name_or_surname(user_name):
                self._view.set_valid_name(False)
                self._view.set_valid_label(False, Translator.translate('Errors.InvalidName'))
                return
            last_name = self._view.get_last_name()
            if not self._is_valid_name_or_surname(last_name):
                self._view.set_valid_last_name(False)
                self._view.set_valid_label(False, Translator.translate('Errors.InvalidLastName'))
                return
            mail = self._view.get_mail()
            if not self._is_valid_mail(mail):
                self._view.set_valid_mail(False)
                self._view.set_valid_label(False, Translator.translate('Errors.InvalidMail'))
                return
            password = self._view.get_password()
            repeat_password = self._view.get_repeat_password()
            if not password == repeat_password:
                self._view.set_valid_password(False)
                self._view.set_valid_label(False, Translator.translate('Errors.PasswordsNotMatch'))
                return
            if not self._is_password_valid(password):
                self._view.set_valid_password(False)
                self._view.set_valid_label(False, Translator.translate('Errors.InvalidPassword'))
                return
            password_hash = bcrypt.hashpw(password.strip().encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            self._db.add_new_user(user_name, last_name, mail, password_hash)
            self._after_login_callback()
        except DBUserWithThisEmailExist:
            self._view.set_valid_name(True)
            self._view.set_valid_last_name(True)
            self._view.set_valid_mail(False)
            self._view.set_valid_password(True)
            self._view.set_valid_label(False, Translator.translate('Errors.UserWithThisMailExist'))
        except DBUnableToInsertData as e:
            self._view.show_error(str(e))
        except:
            self._view.show_error(Translator.translate('Errors.SomethingWentWrong'))

    @staticmethod
    def _is_password_valid(password: str) -> bool:
        return bool(re.match(r"^(?=.*[a-z])(?=.*[0-9]).{8,}$", password))

    @staticmethod
    def _is_valid_name_or_surname(text: str) -> bool:
        return bool(re.match(r"^[a-zA-Z]{2,}$", text))

    @staticmethod
    def _is_valid_mail(mail: str) -> bool:
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(email_regex, mail))
