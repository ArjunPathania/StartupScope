# app/api/v1/endpoints/companies.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import Annotated
from app.dependencies import get_db
from app.schemas.company import CompanyBase
from app.models import Company

router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/")
def read_companies():
    return {"message": "Company list will go here"}

@router.post("/", response_model=CompanyBase, status_code=201)
async def create_company(transaction: CompanyBase, db: db_dependency):
    try:
        data = transaction.dict()   

        if data.get("website"):
            data["website"] = str(data["website"]) 

        new_company = Company(**data)

        db.add(new_company)
        db.commit()
        db.refresh(new_company)
        return new_company
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Failed to create company: {str(e)}")

