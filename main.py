from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel 
import uvicorn

# creating instance of fastapi
app = FastAPI() 

# @app.get("/blog?limit=10&published=true")
# def index():
#     # will get 10 published blogs
#     return{"data": "blog list"}

@app.get("/blog")
def index(limit=10,published:bool=True,sort: Optional[str]=None):
    # will get 10 published blogs
    if published:
        return {'data':f'{limit} published blogs from the db'}
    else:
        return{'data':f'{limit}blogs from the db'}

# dynamic routing
@app.get("/blog/{id}")
def show(id:int):
    return{"data": id}


@app.get("/blog/{id}/comments") 
def show(id):
    return{"data": {'1','2'}}

# we are creating post request
class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]

@app.post('/blog')
def create_blog(blog:Blog):
    # return request
    return {'data':f"blog is created with title as {blog.title}"}

# for debugging purpose bcoz when we debug hamare 8000 pe chal server chal rah hoga
# if __name__ =="__main___":
#     uvicorn.run(app,host="127.0.0.1",port=9000)

