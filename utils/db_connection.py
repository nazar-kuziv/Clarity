from dotenv import dotenv_values
from supabase import create_client, Client

from utils.environment import Environment
from utils.exceptions.db_unable_to_connect import DBUnableToConnect
from utils.exceptions.db_unable_to_get_data import DBUnableToGetData


class DBConnectionMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DBConnection(metaclass=DBConnectionMeta):
    def __init__(self):
        env_vars = dotenv_values(Environment.resource_path(".env"))
        url = env_vars.get("SUPABASE_URL")
        key = env_vars.get("SUPABASE_KEY")
        try:
            self.client: Client = create_client(url, key)
        except Exception:
            raise DBUnableToConnect()

    def get_user(self, email: str):
        try:
            return self.client.table("users").select("*").eq("email", email).execute()
        except:
            raise DBUnableToGetData()
