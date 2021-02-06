from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.response import ResponseCreateMessageDto
from db.database import DBSession
from db.exceptions import DBMessageNotExistsException
from db.queries import message as message_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicMessageNotFound


class OneMessageEndpoint(BaseEndpoint):

    async def method_get(
            self, request: Request, body: dict, session: DBSession, mid: int, *args, **kwargs
    ) -> BaseHTTPResponse:

        try:
            db_message = message_queries.get_messages(session, mid)
        except DBMessageNotExistsException:
            raise SanicMessageNotFound('Message not found')
        response_model = ResponseCreateMessageDto(db_message)

        return await self.make_response_json(status=200, body=response_model.dump())
