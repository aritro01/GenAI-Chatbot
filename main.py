"""Main Module/ App driver"""
from typing import Annotated
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import db.models as models
from db.database import engine, SessionLocal
from core.schemas import UserBaseModel
import encrypt

app = FastAPI()

#Binding to DB and create all the schemas
models.Base.metadata.create_all(bind=engine)

def get_data():
    """method to fetch data from db"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

DbContext = Annotated[Session, Depends(get_data)]

@app.post("/register/")
async def register_user(user: UserBaseModel, db: DbContext):
    """Register new user endpoint"""
    new_user = models.Users(emailID=user.emailID,
                            role=user.role,
                            projectID=user.projectID,
                            password=encrypt.hash_password(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

@app.post("/login/")
async def login_user(user: UserBaseModel, db: DbContext):
    """Login user endpoint"""
    user_record = db.query(models.Users).filter(models.Users.emailID == user.emailID).first()
    if not user_record:
        return HTTPException(status_code=404, detail={"message": "User not found"})
    else:
        if encrypt.verify_hash(user.password, user_record.password):
            return HTTPException(status_code=200, detail={"message": "Login successful"})
        else:
            return HTTPException(status_code=403, detail={"message": "Incorrect Credentials"})
