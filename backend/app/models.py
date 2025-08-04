from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, Text, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(String, nullable=False)
    department = Column(String)
    manager_id = Column(Integer, ForeignKey("employees.id"), nullable=True)
    # Relationships
    manager = relationship("Employee", remote_side=[id], backref="team_members")

class Goal(Base):
    __tablename__ = "goals"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(Text)
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String)
    progress = Column(Float, default=0.0)
    employee = relationship("Employee", backref="goals")

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    reviewer_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    period = Column(String)
    feedback = Column(Text)
    rating = Column(Float)
    type = Column(String)  # self/peer/manager
    employee = relationship("Employee", foreign_keys=[employee_id], backref="reviews_received")
    reviewer = relationship("Employee", foreign_keys=[reviewer_id], backref="reviews_given")

class Skill(Base):
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text)

class EmployeeSkill(Base):
    __tablename__ = "employee_skills"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    skill_id = Column(Integer, ForeignKey("skills.id"), nullable=False)
    level = Column(String)
    last_assessed = Column(Date)
    employee = relationship("Employee", backref="skills")
    skill = relationship("Skill", backref="employees")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False, default="employee")  # employee, manager, HR
    is_active = Column(Boolean, default=True) 