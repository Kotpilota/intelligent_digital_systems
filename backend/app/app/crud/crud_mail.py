# from typing import Any, Dict, Optional, Union
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.mail import Mail
from app.schemas.mail import MailCreate, MailUpdate
# from app.db.session import SessionLocal
# from sqlalchemy import select
# from typing import List, Type
# from fastapi.encoders import jsonable_encoder


class CRUDMail(CRUDBase[Mail, MailCreate, MailUpdate]):
    model = Mail

    def __init__(self):
        super().__init__(Mail)


mail = CRUDMail()
