from fastapi import FastAPI
from app.routers import users
app = FastAPI()

# Register routers
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}
