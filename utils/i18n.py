import glob
import json
import os
from typing import Optional

from utils.environment import Environment


class Translator:
    _data = {}
    _locale = 'pl'

    @staticmethod
    def initialize(locale: str = 'pl'):
        Translator._locale = locale
        files = glob.glob(os.path.join(Environment.resource_path('static/locales'), f'*.json'))
        for fil in files:
            file_name_without_extension = os.path.splitext(os.path.basename(fil))[0]
            with open(fil, 'r', encoding='utf8') as f:
                Translator._data[file_name_without_extension] = json.load(f)
        if locale not in Translator._data:
            raise Exception('Invalid locale')

    @staticmethod
    def set_locale(loc: str):
        if len(Translator._data) == 0:
            Translator.initialize(loc)
        else:
            if loc in Translator._data:
                Translator._locale = loc
            else:
                raise Exception('Invalid locale')

    @staticmethod
    def get_locale() -> str:
        return Translator._locale

    @staticmethod
    def translate(key: str) -> Optional[str]:
        if len(Translator._data) == 0:
            Translator.initialize()

        keys = key.split('.')
        data = Translator._data.get(Translator._locale, {})

        for k in keys:
            data = data.get(k)
            if data is None:
                return None

        return data
