# from sqlalchemy import Integer, String, Column, Boolean, Float
# from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.orm import Mapped, mapped_column # relationship
from app.db.base_class import Base


class Mail(Base):
    __tablename__ = 'mails'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str]
    phone: Mapped[str]
    mail: Mapped[str]
    description: Mapped[str]
    file_path: Mapped[str]
