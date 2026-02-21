from fastapi import FastAPI, status, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import engine, get_db

# -------------------------------
# CREATE TABLES
# -------------------------------
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# -------------------------------
# ROOT ENDPOINT
# -------------------------------
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI + PostgreSQL API with SQLAlchemy"}

# -------------------------------
# GET ALL POSTS
# -------------------------------
@app.get("/posts", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts

# -------------------------------
# CREATE POST
# -------------------------------
@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# -------------------------------
# GET POST BY ID
# -------------------------------
@app.get("/posts/{id}", response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} was not found"
        )
    
    return post

# -------------------------------
# DELETE POST BY ID
# -------------------------------
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    
    if post.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} does not exist"
        )
    
    post.delete(synchronize_session=False)
    db.commit()
    
    return {"message": "Post deleted successfully"}

# -------------------------------
# UPDATE POST BY ID
# -------------------------------
@app.put("/posts/{id}", response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    
    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} does not exist"
        )
    
    post_query.update(updated_post.model_dump(), synchronize_session=False)
    db.commit()
    
    return post_query.first()