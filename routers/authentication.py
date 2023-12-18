from fastapi import APIRouter, status, Depends, HTTPException
import schemas, database, models
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/login",
    tags=["authentication"]
)

get_db = database.get_db


@router.post('/')
def create_auth(request: schemas.Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(
        models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    return user

