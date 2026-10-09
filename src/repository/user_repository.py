import sqlite3
from src.models.user import User


class UserRepository:
    def __init__(self, db_path):
        self.db_path = db_path

    def _get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    def get_all(self):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, login, full_name, role_id FROM Users")
        rows = cursor.fetchall()
        conn.close()
        return [User(*row) for row in rows]

    def get_by_id(self, user_id):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, login, full_name, role_id FROM Users WHERE id = ?",
            (user_id,)
        )
        row = cursor.fetchone()
        conn.close()
        return User(*row) if row else None

    def get_executors(self):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, login, full_name, role_id FROM Users WHERE role_id = 3"
        )
        rows = cursor.fetchall()
        conn.close()
        return [User(*row) for row in rows]