class UserSessionMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class UserSession(metaclass=UserSessionMeta):
    def set_user_data(self, user_id: int, email: str, name: str, last_name: str):
        self.user_id = user_id
        self.email = email
        self.name = name if name else ''
        self.last_name = last_name if last_name else ''
