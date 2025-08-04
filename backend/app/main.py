from fastapi import FastAPI
from .routers import employees, goals, reviews, skills, auth

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(employees.router, prefix="/employees", tags=["employees"])
app.include_router(goals.router, prefix="/goals", tags=["goals"])
app.include_router(reviews.router, prefix="/reviews", tags=["reviews"])
app.include_router(skills.router, prefix="/skills", tags=["skills"])

@app.get("/")
def read_root():
    return {"msg": "Employee PMS API is running"} 