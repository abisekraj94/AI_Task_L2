from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database
from typing import List
from ..routers.auth import get_current_user, require_role

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Goal, dependencies=[Depends(require_role(["employee", "manager", "HR"]))])
def create_goal(goal: schemas.GoalCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    # Only allow if current_user is the employee or is manager/HR
    if current_user.role == "employee" and current_user.id != goal.employee_id:
        raise HTTPException(status_code=403, detail="Employees can only create their own goals")
    db_goal = models.Goal(**goal.dict())
    db.add(db_goal)
    db.commit()
    db.refresh(db_goal)
    return db_goal

@router.get("/", response_model=List[schemas.Goal], dependencies=[Depends(get_current_user)])
def read_goals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Goal).offset(skip).limit(limit).all()

@router.get("/{goal_id}", response_model=schemas.Goal, dependencies=[Depends(get_current_user)])
def read_goal(goal_id: int, db: Session = Depends(get_db)):
    goal = db.query(models.Goal).filter(models.Goal.id == goal_id).first()
    if not goal:
        raise HTTPException(status_code=404, detail="Goal not found")
    return goal

@router.put("/{goal_id}", response_model=schemas.Goal, dependencies=[Depends(require_role(["employee", "manager", "HR"]))])
def update_goal(goal_id: int, goal: schemas.GoalCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_goal = db.query(models.Goal).filter(models.Goal.id == goal_id).first()
    if not db_goal:
        raise HTTPException(status_code=404, detail="Goal not found")
    # Only allow if current_user is the employee or is manager/HR
    if current_user.role == "employee" and current_user.id != db_goal.employee_id:
        raise HTTPException(status_code=403, detail="Employees can only update their own goals")
    for key, value in goal.dict().items():
        setattr(db_goal, key, value)
    db.commit()
    db.refresh(db_goal)
    return db_goal

@router.delete("/{goal_id}", dependencies=[Depends(require_role(["manager", "HR"]))])
def delete_goal(goal_id: int, db: Session = Depends(get_db)):
    db_goal = db.query(models.Goal).filter(models.Goal.id == goal_id).first()
    if not db_goal:
        raise HTTPException(status_code=404, detail="Goal not found")
    db.delete(db_goal)
    db.commit()
    return {"ok": True} 