from __future__ import annotations

from datetime import datetime
from pathlib import Path

import xlsxwriter

from utils.exceptions.xls_export_failed import XlsExportFailed
from utils.i18n import Translator


class DiaryEntry:
    def __init__(self, db_object: dict):
        self.id = db_object.get("id")
        self.entry_text = db_object.get("entry_text")
        creation_date = db_object.get("creation_date")
        if creation_date:
            self.creation_date = datetime.strptime(creation_date, "%Y-%m-%dT%H:%M:%S")
        self.sentiment = db_object.get("sentiment")
        self.user_id = db_object.get("user_id")

    @staticmethod
    def export_list_to_xls(data: list[DiaryEntry], file_path, hide_content=False):
        try:
            file_path = Path(file_path)
            file_path.parent.mkdir(parents=True, exist_ok=True)

            workbook = xlsxwriter.Workbook(file_path)
            worksheet = workbook.add_worksheet()
            column_names = [Translator.translate('Entry.Content'),
                            Translator.translate('Entry.Sentiment'),
                            Translator.translate('Entry.Date')]

            for i in range(len(column_names)):
                worksheet.write(0, i, column_names[i])

            for i, obj in enumerate(data):
                if not hide_content:
                    worksheet.write(i + 1, 0, obj.entry_text)
                worksheet.write(i + 1, 1, obj.creation_date.strftime("%Y-%m-%d %H:%M") if obj.creation_date else "")
                worksheet.write(i + 1, 2, obj.sentiment)

            worksheet.autofit()
            workbook.close()
        except Exception:
            raise XlsExportFailed()
