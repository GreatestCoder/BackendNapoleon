from api.request import RequestCreateMessageDto
from db.database import DBSession
from db.models import DBMessage


def create_message(session: DBSession, message: RequestCreateMessageDto) -> DBMessage:
    new_message = DBMessage(
        message=message.message,
        recipient_id=message.recipient_id
    )

    session.add_model(new_message)

    return new_message
