from typing import Any, Dict, Optional, Union

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate

from app.db.session import SessionLocal
from sqlalchemy import select
from typing import List, Type
from fastapi.encoders import jsonable_encoder
from datetime import datetime

class CRUDProject(CRUDBase[Project, ProjectCreate, ProjectUpdate]):

    model = Project

    def __init__(self):
        super().__init__(Project)

    
    @classmethod
    async def create(cls, db: AsyncSession, *, obj_in: ProjectCreate) -> Project:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = cls.model(**obj_in_data)  # type : ignore

        db_obj.started_at = datetime.strptime(db_obj.started_at, "%Y-%m-%dT%H:%M:%S")
        db_obj.deadline = datetime.strptime(db_obj.deadline, "%Y-%m-%dT%H:%M:%S")


        str_started_at = db_obj.started_at.strftime("%d-%m-%Y")
        str_deadline = db_obj.deadline.strftime("%d-%m-%Y")
        
        db_obj.started_at = datetime.strptime(str_started_at, "%d-%m-%Y")
        db_obj.deadline = datetime.strptime(str_deadline, "%d-%m-%Y")

        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj
    

    @classmethod
    async def update(cls, db: AsyncSession, *, db_obj: Project, obj_in: Union[ProjectUpdate, Dict[str, Any]]) -> Project:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

  
        db_obj.started_at = datetime.strptime(db_obj.started_at, "%Y-%m-%dT%H:%M:%S")
        db_obj.deadline = datetime.strptime(db_obj.deadline, "%Y-%m-%dT%H:%M:%S")


        str_started_at = db_obj.started_at.strftime("%d-%m-%Y")
        str_deadline = db_obj.deadline.strftime("%d-%m-%Y")
        
        db_obj.started_at = datetime.strptime(str_started_at, "%d-%m-%Y")
        db_obj.deadline = datetime.strptime(str_deadline, "%d-%m-%Y")



        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj


project = CRUDProject()
