import sqlite3
from src.models.ticket import Ticket


class TicketRepository:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_all(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Requests")
        rows = cursor.fetchall()
        conn.close()
        return [Ticket(*row) for row in rows]

    def get_by_id(self, ticket_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Requests WHERE id = ?", (ticket_id,))
        row = cursor.fetchone()
        conn.close()
        return Ticket(*row) if row else None

    def create(self, ticket):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Requests (title, description, category_id, status_id, author_id) "
            "VALUES (?, ?, ?, ?, ?)",
            (ticket.title, ticket.description, ticket.category_id,
             ticket.status_id, ticket.author_id)
        )
        conn.commit()
        ticket.id = cursor.lastrowid
        conn.close()
        return ticket

    def update_status(self, ticket_id, status_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Requests SET status_id = ? WHERE id = ?",
            (status_id, ticket_id)
        )
        conn.commit()
        conn.close()

    def delete(self, ticket_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Requests WHERE id = ?", (ticket_id,))
        conn.commit()
        conn.close()
    def search(self, query):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, title, description, category_id, status_id, author_id, assignee_id "
            "FROM Requests "
            "WHERE title LIKE ? OR description LIKE ?",
            (f"%{query}%", f"%{query}%")
        )
        rows = cursor.fetchall()
        conn.close()
        return [Ticket(*row) for row in rows]

    def filter_by_status(self, status_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, title, description, category_id, status_id, author_id, assignee_id "
            "FROM Requests WHERE status_id = ?",
            (status_id,)
        )
        rows = cursor.fetchall()
        conn.close()
        return [Ticket(*row) for row in rows]

    def filter_by_category(self, category_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, title, description, category_id, status_id, author_id, assignee_id "
            "FROM Requests WHERE category_id = ?",
            (category_id,)
        )
        rows = cursor.fetchall()
        conn.close()
        return [Ticket(*row) for row in rows]