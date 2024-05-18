from fastapi import FastAPI,Depends ,status,Response,HTTPException,APIRouter
from .. import schemas,models,database
from sqlalchemy.orm import Session
from typing import List
from passlib.context import CryptContext
router = APIRouter(
    prefix="/user",
    tags=['users']
)

get_db=database.get_db

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post('/',response_model=schemas.ShowUser)
def create_user(request:schemas.User,db:Session = Depends(get_db)):
    hashedPassword=pwd_context.hash(request.password)
    new_user = models.User(name=request.name,email=request.email,password=hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db:Session = Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog of id {id} not found")
    return user