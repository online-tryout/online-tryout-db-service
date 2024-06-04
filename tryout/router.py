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
        return tryouts
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/{tryout_id}")
def get_tryout(tryout_id: str, db: Session = Depends(get_db)):
    try:
        tryout = crud.get_tryout(db, tryout_id)
        if tryout is None:
            raise HTTPException(status_code=404, detail="Tryout not found")
        return tryout
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{tryout_id}/{module_id}")
def get_module(module_id: str, db: Session = Depends(get_db)):
    try:
        module = crud.get_module_by_id(db, module_id)
        if module:
            return module
        raise HTTPException(status_code=404, detail="module not found")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))