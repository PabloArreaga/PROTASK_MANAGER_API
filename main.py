from fastapi import FastAPI
from app.routers import router

app = FastAPI()

# Registrar los routers
app.include_router(router)

# Punto de entrada para la aplicación
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)