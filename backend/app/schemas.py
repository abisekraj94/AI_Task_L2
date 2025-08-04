from pydantic import BaseModel, EmailStr
from typing import Optional, List, Any
from datetime import date

class EmployeeBase(BaseModel):
    name: str
    email: EmailStr
    role: str
    department: Optional[str] = None
    manager_id: Optional[int] = None

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int
    class Config:
        orm_mode = True

class GoalBase(BaseModel):
    title: str
    description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    status: Optional[str] = None
    progress: Optional[float] = 0.0

class GoalCreate(GoalBase):
    employee_id: int

class Goal(GoalBase):
    id: int
    employee_id: int
    class Config:
        orm_mode = True

class ReviewBase(BaseModel):
    period: Optional[str] = None
    feedback: Optional[str] = None
    rating: Optional[float] = None
    type: Optional[str] = None

class ReviewCreate(ReviewBase):
    employee_id: int
    reviewer_id: int

class Review(ReviewBase):
    id: int
    employee_id: int
    reviewer_id: int
    class Config:
        orm_mode = True

class SkillBase(BaseModel):
    name: str
    description: Optional[str] = None

class SkillCreate(SkillBase):
    pass

class Skill(SkillBase):
    id: int
    class Config:
        orm_mode = True

class EmployeeSkillBase(BaseModel):
    employee_id: int
    skill_id: int
    level: Optional[str] = None
    last_assessed: Optional[date] = None

class EmployeeSkillCreate(EmployeeSkillBase):
    pass

class EmployeeSkill(EmployeeSkillBase):
    id: int
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: str = "employee"

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class User(UserBase):
    id: int
    is_active: bool
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str 