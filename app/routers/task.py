from fastapi import APIRouter, HTTPException
from app.schemas.task import TaskCreate, TaskUpdate
from app.services.task_service import TaskService
from typing import List

router = APIRouter()

# Instancia del servicio de tareas (Singleton)
task_service = TaskService()

@router.post("/tareas", response_model=dict)
def create_task(task: TaskCreate):
    try:
        task_id = task_service.create_task(task)
        return {"id": task_id, "message": "Tarea creada exitosamente"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/tareas", response_model=List[dict])
def get_tasks(status: str = None, priority: str = None, assigned_user: str = None):
    tasks = task_service.get_tasks(status=status, priority=priority, assigned_user=assigned_user)
    return tasks


@router.get("/tareas/{id}", response_model=dict)
def get_task(id: int):
    task = task_service.get_task(id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task


@router.put("/tareas/{id}", response_model=dict)
def update_task(id: int, task: TaskUpdate):
    try:
        task_service.update_task(id, task)
        return {"message": "Tarea actualizada exitosamente"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/tareas/{id}", response_model=dict)
def delete_task(id: int):
    try:
        task_service.delete_task(id)
        return {"message": "Tarea eliminada exitosamente"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
