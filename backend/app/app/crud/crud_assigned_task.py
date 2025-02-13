from typing import Any, Dict, Optional, Union

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.assigned_task import Assigned_Task
from app.schemas.assigned_task import Assigned_Task, Assigned_TaskUpdate

from app.db.session import SessionLocal
from sqlalchemy import select
from typing import List, Type
from fastapi.encoders import jsonable_encoder


class CRUDAssigned_Task(CRUDBase[Assigned_Task, Assigned_Task, Assigned_TaskUpdate]):

    model = Assigned_Task

    def __init__(self):
        super().__init__(Assigned_Task)


assigned_task = CRUDAssigned_Task()
