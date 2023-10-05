import time
from typing import Optional

from pydantic import BaseModel

from . import models
from .database import engine, get_db
import psycopg2
from sqlalchemy.orm import Session
from fastapi import FastAPI, status, Response, HTTPException, Depends  # Response for the code exit
from psycopg2.extras import RealDictCursor

models.Base.metadata.create_all(bind=engine)

# py -3 -m venv "name" -> create the environment
# venv/Scripts/activate.bat -> active the virtual envi
# unicorn main:app -reload -> execute and every time that I update the file it'll refresh automatically
app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
                                password='147258369', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database  connection was successfully\n")
        break
    except Exception as error:
        print('Connection to database failed')
        print('Error: ', error)
        time.sleep(2)


class Post(BaseModel):
    title: str
    content: str
    user: str
    published: bool = True  # value by defect true
    rating: Optional[int] = None  # the attribute is optional allowing that user don't send this
    # if he doesn't want, and validates if the value is an integer


@app.get('/')
def root():
    return {'Message:': 'Hello world Since the main 2 !!'}


@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"Data": "successfully"}


@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"Data": posts}


@app.post("/posts", status_code=status.HTPP_201_CREATED)
def create_post(post: Post, db: Session = Depends(get_db)):
    models.Post(title=post.title)
    return {"Data": {new_post}}
