from typing import Any, Dict, Optional, Union

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.assigned_task import Assigned_Task
from app.schemas.assigned_task import Assigned_TaskCreate, Assigned_TaskUpdate

from app.db.session import SessionLocal
from sqlalchemy import select
from typing import List, Type
from fastapi.encoders import jsonable_encoder
from datetime import datetime

class CRUDAssigned_Task(CRUDBase[Assigned_Task, Assigned_TaskCreate, Assigned_TaskUpdate]):

    model = Assigned_Task

    def __init__(self):
        super().__init__(Assigned_Task)


    @classmethod
    async def create(cls, db: AsyncSession, *, obj_in: Assigned_TaskCreate) -> Assigned_Task:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = cls.model(**obj_in_data)  # type : ignore

        db_obj.assigned_at = datetime.strptime(db_obj.assigned_at, "%Y-%m-%dT%H:%M:%S")
        db_obj.deadline = datetime.strptime(db_obj.deadline, "%Y-%m-%dT%H:%M:%S")


        str_assigned_at = db_obj.assigned_at.strftime("%d-%m-%Y")
        str_deadline = db_obj.deadline.strftime("%d-%m-%Y")
        
        db_obj.assigned_at = datetime.strptime(str_assigned_at, "%d-%m-%Y")
        db_obj.deadline = datetime.strptime(str_deadline, "%d-%m-%Y")

        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj
    

    @classmethod
    async def update(cls, db: AsyncSession, *, db_obj: Assigned_Task, obj_in: Union[Assigned_TaskUpdate, Dict[str, Any]]) -> Assigned_Task:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

        

        str_assigned_at = db_obj.assigned_at.strftime("%d-%m-%Y")
        str_deadline = db_obj.deadline.strftime("%d-%m-%Y")
        
        db_obj.assigned_at = datetime.strptime(str_assigned_at, "%d-%m-%Y")
        db_obj.deadline = datetime.strptime(str_deadline, "%d-%m-%Y")



        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj


assigned_task = CRUDAssigned_Task()
