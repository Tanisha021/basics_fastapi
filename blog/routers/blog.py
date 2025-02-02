from fastapi import FastAPI,Depends ,status,Response,HTTPException,APIRouter
from .. import schemas,models,database
from sqlalchemy.orm import Session
from typing import List
router = APIRouter(
     prefix="/blog",
    tags=['blogs']
)

get_db=database.get_db

@router.get('/',response_model=List[schemas.ShowBlog])
def all(db:Session = Depends(database.get_db)):
    blogs=db.query(models.Blog).all()
    return blogs    

# POST(create)
@router.post('/',status_code=status.HTTP_201_CREATED)
# gonna convert session into pydantic thing
def create(request:schemas.Blog,db:Session = Depends(get_db)):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=1    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# GET BY ID
@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog)
def show(id,response:Response, db:Session = Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog of id {id} not found")
    return blog

# DELETE
@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return "deleted"

# UPDATE
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.Blog,db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog of id {id} not found")
    blog.update(request)
    db.commit()
    return "updated"