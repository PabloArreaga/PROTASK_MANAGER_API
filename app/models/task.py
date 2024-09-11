from datetime import datetime
from typing import Optional

class Task:
    def __init__(self, id: int, title: str, description: Optional[str], created_at: datetime, 
                 deadline: Optional[datetime], priority: str, status: str, 
                 assigned_user: Optional[str], category: str):
        self.id = id
        self.title = title
        self.description = description
        self.created_at = created_at
        self.deadline = deadline
        self.priority = priority
        self.status = status
        self.assigned_user = assigned_user
        self.category = category

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at,
            "deadline": self.deadline,
            "priority": self.priority,
            "status": self.status,
            "assigned_user": self.assigned_user,
            "category": self.category,
        }
