from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from payment import schema, crud

router = APIRouter()


@router.get("/transaction/", response_model=schema.Transaction)
async def get_transaction(transaction_id: str, db: Session = Depends(get_db)):
    try:
        transaction = crud.get_transaction(db, transaction_id)
        if transaction is None:
            raise HTTPException(status_code=404, detail="Transaction not found")
        return transaction
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/transactions/", response_model=list[schema.Transaction])
async def get_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        return crud.get_transactions(db, skip=skip, limit=limit)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/transactions/user/", response_model=list[schema.Transaction])
async def get_transactions_by_user(user_id: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        return crud.get_transactions_by_user(db, user_id, skip=skip, limit=limit)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.get("/transactions/tryout/", response_model=list[schema.Transaction])
async def get_transactions_by_tryout(tryout_id: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        return crud.get_transactions_by_tryout(db, tryout_id, skip=skip, limit=limit)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.post("/transaction/", response_model=schema.Transaction)
async def create_transaction(transaction: schema.TransactionCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_transaction(db, transaction)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.put("/transaction/", response_model=schema.Transaction)
async def update_transaction(transaction_id: str, updated_transaction: schema.TransactionCreate, db: Session = Depends(get_db)):
    try:
        return crud.update_transaction(db, transaction_id, updated_transaction)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    