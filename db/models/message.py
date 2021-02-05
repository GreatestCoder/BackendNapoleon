from sqlalchemy import Column, Integer, VARCHAR
from db.models import BaseModel


class DBMessage(BaseModel):

    __tablename__ = 'messages'

    id = BaseModel.id
    created_at = BaseModel.created_at
    updated_at = BaseModel.updated_at
    message = Column(VARCHAR(200))

    sender_id = Column(
        Integer,
        nullable=False
    )

    recipient_id = Column(
        Integer,
        nullable=False
    )
