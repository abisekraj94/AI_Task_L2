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

@router.post("/", response_model=schemas.Review, dependencies=[Depends(require_role(["manager", "HR"]))])
def create_review(review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    db_review = models.Review(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

@router.get("/", response_model=List[schemas.Review], dependencies=[Depends(get_current_user)])
def read_reviews(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Review).offset(skip).limit(limit).all()

@router.get("/{review_id}", response_model=schemas.Review, dependencies=[Depends(get_current_user)])
def read_review(review_id: int, db: Session = Depends(get_db)):
    review = db.query(models.Review).filter(models.Review.id == review_id).first()
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review

@router.put("/{review_id}", response_model=schemas.Review, dependencies=[Depends(require_role(["manager", "HR"]))])
def update_review(review_id: int, review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    db_review = db.query(models.Review).filter(models.Review.id == review_id).first()
    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found")
    for key, value in review.dict().items():
        setattr(db_review, key, value)
    db.commit()
    db.refresh(db_review)
    return db_review

@router.delete("/{review_id}", dependencies=[Depends(require_role(["manager", "HR"]))])
def delete_review(review_id: int, db: Session = Depends(get_db)):
    db_review = db.query(models.Review).filter(models.Review.id == review_id).first()
    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found")
    db.delete(db_review)
    db.commit()
    return {"ok": True} 