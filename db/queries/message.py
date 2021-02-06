
from api.request import RequestCreateMessageDto, RequestPatchMessageDto
from db.database import DBSession
from db.models import DBMessage


def create_message(session: DBSession, message: RequestCreateMessageDto) -> DBMessage:
    new_message = DBMessage(
        message=message.message,
        recipient_id=message.recipient_id,
        sender_id=message.sender_id
    )

    session.add_model(new_message)

    return new_message


def patch_message(session: DBSession, message: RequestPatchMessageDto, message_id: int) -> DBMessage:
    db_message = session.get_message_by_id(message_id)

    for attr in message.fields:
        if hasattr(message, attr):
            value = getattr(message, attr)
            setattr(db_message, attr, value)

    return db_message


def delete_message(session: DBSession, message_id: int) -> DBMessage:
    db_message = session.get_message_by_id(message_id)
    db_message.is_delete = True
    return db_message


def get_messages(session: DBSession, message_id: int) -> DBMessage:
    return session.get_message_by_id(message_id)
