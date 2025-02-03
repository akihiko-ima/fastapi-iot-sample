from fastapi import APIRouter, Path, Query, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import Annotated

from database import get_db
from models import SensorData

# 依存性の注入
DbDependency = Annotated[Session, Depends(get_db)]


router = APIRouter(prefix="/sensor", tags=["sensor"])


# クエリパラーメータの例: http://127.0.0.1:8000/sensor?machineID=1&temperature=20.3
@router.get("")
def add_data(machineID: int, temperature: float, db: DbDependency):
    new_data = SensorData(machineID=machineID, temperature=temperature)
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return {"message": "Data saved successfully", "data": new_data}
