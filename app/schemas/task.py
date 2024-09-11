from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=5, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    created_at: datetime = Field(..., description="La fecha de creación de la tarea, no puede ser una fecha futura")
    deadline: Optional[datetime] = Field(None, description="Debe ser una fecha futura")
    priority: str = Field(..., regex="^(Baja|Media|Alta)$")
    status: str = Field(..., regex="^(Pendiente)$")
    assigned_user: Optional[str] = None
    category: str = Field(..., regex="^(Administración|Ventas|Soporte|Desarrollo)$")

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=5, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    deadline: Optional[datetime] = Field(None, description="Debe ser una fecha futura")
    priority: Optional[str] = Field(None, regex="^(Baja|Media|Alta)$")
    status: Optional[str] = Field(None, regex="^(Pendiente|En Proceso|Completada|Cancelada)$")
    assigned_user: Optional[str] = None
    category: Optional[str] = Field(None, regex="^(Administración|Ventas|Soporte|Desarrollo)$")

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    created_at: datetime
    deadline: Optional[datetime]
    priority: str
    status: str
    assigned_user: Optional[str]
    category: str

    class Config:
        orm_mode = True
