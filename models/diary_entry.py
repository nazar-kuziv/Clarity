from datetime import datetime


class DiaryEntry:
    def __init__(self, db_object: dict):
        self.id = db_object.get("id")
        self.entry_text = db_object.get("entry_text")
        creation_date = db_object.get("creation_date")
        if creation_date:
            self.creation_date = datetime.strptime(creation_date, "%Y-%m-%dT%H:%M:%S")
        self.sentiment = db_object.get("sentiment")
        self.user_id = db_object.get("user_id")