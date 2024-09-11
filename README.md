# PROTASK_MANAGER_API


## Descripción

La **PROTASK_MANAGER_API** es una API RESTful diseñada para gestionar tareas o procesos dentro de una empresa. Esta API permite crear, leer, actualizar y eliminar tareas en memoria utilizando un patrón de almacenamiento volátil basado en el patrón Singleton. La API está optimizada para ser escalable, manteniendo una estructura modular, y permite manejar tareas con varios atributos, incluyendo prioridades, categorías y usuarios asignados.

## Funcionalidades

1. **Creación de Tarea** (POST `/tareas`)
   - Crea una nueva tarea con los siguientes campos:
     - **Título**: Obligatorio. Entre 5 y 100 caracteres.
     - **Descripción**: Opcional. Máximo 500 caracteres.
     - **Fecha de creación**: Obligatorio. No puede ser una fecha futura.
     - **Fecha límite**: Opcional. Debe ser una fecha futura si se proporciona.
     - **Prioridad**: Obligatorio. Puede ser "Baja", "Media", "Alta".
     - **Estado**: Obligatorio. Inicia como "Pendiente". Los posibles estados son "Pendiente", "En Proceso", "Completada", "Cancelada".
     - **Usuario asignado**: Opcional. Debe corresponder al ID de un usuario existente si se proporciona.
     - **Categoría**: Obligatorio. Debe seleccionarse de una lista predefinida ("Administración", "Ventas", "Soporte", "Desarrollo").

2. **Lectura de Tareas** (GET `/tareas`)
   - Recupera todas las tareas registradas. Permite filtrar por:
     - Estado de la tarea: "Pendiente", "En Proceso", "Completada", "Cancelada".
     - Prioridad: "Baja", "Media", "Alta".
     - Fecha límite: Filtra por un rango de fechas.
     - Usuario asignado: Filtra por el ID del empleado asignado.

3. **Lectura de una Tarea Específica** (GET `/tareas/{id}`)
   - Recupera la información de una tarea específica usando su ID.

4. **Actualización de Tarea** (PUT `/tareas/{id}`)
   - Actualiza una tarea existente. Se validan las mismas restricciones que en la creación. Se permite cambiar el estado de la tarea bajo las siguientes reglas:
     - Solo se puede marcar una tarea como "Completada" si está en estado "En Proceso".
     - No se pueden modificar tareas que estén en estado "Completada" o "Cancelada".

5. **Eliminación de Tarea** (DELETE `/tareas/{id}`)
   - Permite eliminar una tarea específica. No se pueden eliminar tareas que estén en estado "Completada" o "Cancelada".

## Requisitos Previos

- **Python 3.8+**
- **FastAPI** para manejar las rutas.
- **Pydantic** para la validación de datos.

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu-usuario/project_management_api.git


## Esquema para el proyecto
/project_management_api
│
├── /app
│   ├── /routers
│   │   └── tasks.py        # Aquí van las rutas relacionadas con las tareas
│   │
│   ├── /models
│   │   └── task.py         # Definición del modelo de datos de la tarea
│   │
│   ├── /schemas
│   │   └── task.py         # Esquemas Pydantic para validaciones y serialización
│   │
│   ├── /services
│   │   └── task_service.py  # Lógica de negocio para la creación, lectura, actualización y eliminación de tareas
│   │
│   └── /storage
│       └── singleton.py    # Implementación del patrón Singleton para almacenamiento volátil
│
├── /resources              # Archivos complementarios
│
├── /tests
│   └── test_tasks.py        # Tests unitarios y funcionales para las rutas y servicios
│
├── .env                    # Variables de entorno
├── main.py                 # Punto de entrada principal para la API
└── requirements.txt        # Dependencias del proyecto

