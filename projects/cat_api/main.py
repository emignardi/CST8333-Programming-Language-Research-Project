from fastapi import FastAPI, status, HTTPException
import uvicorn
from pydantic import BaseModel
from typing import Optional
from db import engine, Session
from models import Base, Cat

app = FastAPI()
Base.metadata.create_all(bind=engine)

class CatModel(BaseModel):
    id: Optional[int] = None
    name: str
    colour: str

class CatUpdateModel(BaseModel):
    name: Optional[str]
    colour: Optional[str]


@app.get("/cats", response_model=list[CatModel], status_code=status.HTTP_200_OK)
def findAll():
    with Session() as session:
        cats = session.query(Cat).all()
        if cats:
            return cats
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
@app.get("/cats/{id}", response_model=CatModel, status_code=status.HTTP_200_OK)
def findById(id: int):
    with Session() as session:
        cat = session.query(Cat).filter(Cat.id == id).first()
        if cat:
            return cat
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
@app.post("/cats", status_code=status.HTTP_201_CREATED)
def create(cat: CatModel):
    with Session() as session:
        newCat = Cat(**cat.model_dump())
        session.add(newCat)
        session.commit()

@app.delete("/cats/{id}", status_code=status.HTTP_200_OK)
def delete(id: int):
    with Session() as session:
        cat = session.query(Cat).filter(Cat.id == id).first()
        if cat:
            session.delete(cat)
            session.commit()
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
@app.put("/cats/{id}", status_code=status.HTTP_200_OK)
def update(id: int, updatedCat: CatUpdateModel):
    with Session() as session:
        cat = session.query(Cat).filter(Cat.id == id).first()
        if cat:
            cat.name = updatedCat.name
            cat.colour = updatedCat.colour
            session.add(cat)
            session.commit()
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        
def main():
    uvicorn.run(app)

if __name__ == "__main__":
    main()