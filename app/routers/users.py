from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def get_users():
    return {"message": "List of users"}

@router.get("/{user_id}")
def get_user(user_id: int):
    return {"message": f"User {user_id}"}

@router.post("/")
def create_user(user: dict):
    return {"message": "User created", "user": user}
