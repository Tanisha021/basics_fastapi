from pydantic import BaseModel
from typing import Optional,List

class Blog(BaseModel):
    title:str
    body:str
    class Config():
        orm_model = True
# class ShowBlog(Blog):
#     class Config():
#         orm_model = True

class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    blogs:List
    class Config():
        orm_model = True

class ShowBlog(BaseModel):
    title:str
    body:str
    creator:ShowUser
    class Config():
        orm_model = True
