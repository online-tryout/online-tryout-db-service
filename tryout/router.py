from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from tryout import schemas, crud

router = APIRouter()

@router.post("")
async def create_tryout(tryout_params: schemas.CreateTryoutParams, db: Session = Depends(get_db)):
    try:
        return crud.create_tryout(db, tryout_params)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("")
def get_tryouts(db: Session = Depends(get_db)):
    try:
        tryouts = crud.get_all_tryouts(db)
        return schemas.TryoutResponse(tryouts=tryouts, message="Tryouts fetched successfully")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
