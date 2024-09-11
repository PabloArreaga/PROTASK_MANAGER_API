from datetime import datetime
from typing import List, Optional
from app.models.task import Task
from app.storage.singleton import SingletonStorage
from app.schemas.task import TaskCreate, TaskUpdate

class TaskService:
    def __init__(self):
        self.storage = SingletonStorage()

    def create_task(self, task_data: TaskCreate) -> int:
        # Validar que la fecha de creación no sea en el futuro
        if task_data.created_at > datetime.now():
            raise ValueError("La fecha de creación no puede ser una fecha futura.")
        # Validar que la fecha límite, si existe, sea en el futuro
        if task_data.deadline and task_data.deadline <= datetime.now():
            raise ValueError("La fecha límite debe ser una fecha futura.")
        
        # Crear la tarea
        task_id = self.storage.get_next_id()
        task = Task(
            id=task_id,
            title=task_data.title,
            description=task_data.description,
            created_at=task_data.created_at,
            deadline=task_data.deadline,
            priority=task_data.priority,
            status=task_data.status,
            assigned_user=task_data.assigned_user,
            category=task_data.category,
        )
        self.storage.add_task(task)
        return task_id

    def get_tasks(self, status: Optional[str] = None, priority: Optional[str] = None, 
                  assigned_user: Optional[str] = None) -> List[dict]:
        tasks = self.storage.get_all_tasks()
        # Filtrar por estado, prioridad, y usuario asignado si se proporcionan
        if status:
            tasks = [task for task in tasks if task.status == status]
        if priority:
            tasks = [task for task in tasks if task.priority == priority]
        if assigned_user:
            tasks = [task for task in tasks if task.assigned_user == assigned_user]
        return [task.to_dict() for task in tasks]

    def get_task(self, task_id: int) -> Optional[dict]:
        task = self.storage.get_task(task_id)
        if task:
            return task.to_dict()
        return None

    def update_task(self, task_id: int, task_data: TaskUpdate):
        task = self.storage.get_task(task_id)
        if not task:
            raise ValueError("La tarea no existe.")
        
        # Actualizar los campos de la tarea
        if task_data.title:
            task.title = task_data.title
        if task_data.description:
            task.description = task_data.description
        if task_data.deadline:
            if task_data.deadline <= datetime.now():
                raise ValueError("La fecha límite debe ser una fecha futura.")
            task.deadline = task_data.deadline
        if task_data.priority:
            task.priority = task_data.priority
        if task_data.status:
            # Restringir cambios de estado de acuerdo con las reglas
            if task.status in ["Completada", "Cancelada"]:
                raise ValueError("No se puede modificar una tarea Completada o Cancelada.")
            if task_data.status == "Completada" and task.status != "En Proceso":
                raise ValueError("Solo se puede completar una tarea que esté en proceso.")
            task.status = task_data.status
        if task_data.assigned_user:
            task.assigned_user = task_data.assigned_user
        if task_data.category:
            task.category = task_data.category
        
        self.storage.update_task(task)

    def delete_task(self, task_id: int):
        task = self.storage.get_task(task_id)
        if not task:
            raise ValueError("La tarea no existe.")
        if task.status in ["Completada", "Cancelada"]:
            raise ValueError("No se puede eliminar una tarea que ya está Completada o Cancelada.")
        self.storage.delete_task(task_id)
