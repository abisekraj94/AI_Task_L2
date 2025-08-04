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

# Skill CRUD
@router.post("/", response_model=schemas.Skill, dependencies=[Depends(require_role(["HR"]))])
def create_skill(skill: schemas.SkillCreate, db: Session = Depends(get_db)):
    db_skill = models.Skill(**skill.dict())
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill

@router.get("/", response_model=List[schemas.Skill], dependencies=[Depends(get_current_user)])
def read_skills(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Skill).offset(skip).limit(limit).all()

@router.get("/{skill_id}", response_model=schemas.Skill, dependencies=[Depends(get_current_user)])
def read_skill(skill_id: int, db: Session = Depends(get_db)):
    skill = db.query(models.Skill).filter(models.Skill.id == skill_id).first()
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    return skill

@router.put("/{skill_id}", response_model=schemas.Skill, dependencies=[Depends(require_role(["HR"]))])
def update_skill(skill_id: int, skill: schemas.SkillCreate, db: Session = Depends(get_db)):
    db_skill = db.query(models.Skill).filter(models.Skill.id == skill_id).first()
    if not db_skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    for key, value in skill.dict().items():
        setattr(db_skill, key, value)
    db.commit()
    db.refresh(db_skill)
    return db_skill

@router.delete("/{skill_id}", dependencies=[Depends(require_role(["HR"]))])
def delete_skill(skill_id: int, db: Session = Depends(get_db)):
    db_skill = db.query(models.Skill).filter(models.Skill.id == skill_id).first()
    if not db_skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    db.delete(db_skill)
    db.commit()
    return {"ok": True}

# EmployeeSkill CRUD
@router.post("/employee-skill/", response_model=schemas.EmployeeSkill, dependencies=[Depends(get_current_user)])
def create_employee_skill(employee_skill: schemas.EmployeeSkillCreate, db: Session = Depends(get_db)):
    db_employee_skill = models.EmployeeSkill(**employee_skill.dict())
    db.add(db_employee_skill)
    db.commit()
    db.refresh(db_employee_skill)
    return db_employee_skill

@router.get("/employee-skill/", response_model=List[schemas.EmployeeSkill], dependencies=[Depends(get_current_user)])
def read_employee_skills(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.EmployeeSkill).offset(skip).limit(limit).all()

@router.get("/employee-skill/{employee_skill_id}", response_model=schemas.EmployeeSkill, dependencies=[Depends(get_current_user)])
def read_employee_skill(employee_skill_id: int, db: Session = Depends(get_db)):
    employee_skill = db.query(models.EmployeeSkill).filter(models.EmployeeSkill.id == employee_skill_id).first()
    if not employee_skill:
        raise HTTPException(status_code=404, detail="EmployeeSkill not found")
    return employee_skill

@router.put("/employee-skill/{employee_skill_id}", response_model=schemas.EmployeeSkill, dependencies=[Depends(get_current_user)])
def update_employee_skill(employee_skill_id: int, employee_skill: schemas.EmployeeSkillCreate, db: Session = Depends(get_db)):
    db_employee_skill = db.query(models.EmployeeSkill).filter(models.EmployeeSkill.id == employee_skill_id).first()
    if not db_employee_skill:
        raise HTTPException(status_code=404, detail="EmployeeSkill not found")
    for key, value in employee_skill.dict().items():
        setattr(db_employee_skill, key, value)
    db.commit()
    db.refresh(db_employee_skill)
    return db_employee_skill

@router.delete("/employee-skill/{employee_skill_id}", dependencies=[Depends(get_current_user)])
def delete_employee_skill(employee_skill_id: int, db: Session = Depends(get_db)):
    db_employee_skill = db.query(models.EmployeeSkill).filter(models.EmployeeSkill.id == employee_skill_id).first()
    if not db_employee_skill:
        raise HTTPException(status_code=404, detail="EmployeeSkill not found")
    db.delete(db_employee_skill)
    db.commit()
    return {"ok": True} 