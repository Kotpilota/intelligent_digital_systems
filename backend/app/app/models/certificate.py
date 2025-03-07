from datetime import datetime
from sqlalchemy import  ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base_class import Base
from  app.models.user import User
from app.models.file import File

class Certificate(Base):

    __tablename__ = "certificates"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    user_id: Mapped[int] = mapped_column( ForeignKey("users.id", ondelete='cascade') )
    file_id: Mapped[int] = mapped_column( ForeignKey("files.id", ondelete='cascade') )

    user:Mapped[User] = relationship("User", lazy="joined", cascade="all")
    file:Mapped[File] = relationship("File", lazy="joined", cascade="all")
