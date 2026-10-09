class Ticket:
    def __init__(self, id, title, description, category_id, status_id,
                 author_id, assignee_id=None, created_at=None, closed_at=None):
        self.id = id
        self.title = title
        self.description = description
        self.category_id = category_id
        self.status_id = status_id
        self.author_id = author_id
        self.assignee_id = assignee_id
        self.created_at = created_at
        self.closed_at = closed_at

    def __repr__(self):
        return f"Ticket(id={self.id}, title={self.title!r})"