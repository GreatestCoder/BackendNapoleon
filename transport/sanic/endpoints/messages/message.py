from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request import RequestPatchMessageDto
from api.response import ResponseCreateMessageDto
from db.database import DBSession
from db.exceptions import DBDataException, DBIntegrityException, DBMessageNotExistsException
from db.queries import message as message_queries
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicDBException, SanicMessageNotFound


class MessageEndpoint(BaseEndpoint):
    async def method_patch(
            self, request: Request, body: dict, session: DBSession, mid: int, *args, **kwargs
    ) -> BaseHTTPResponse:

        request_model = RequestPatchMessageDto(body)

        try:
            message = message_queries.patch_message(session, request_model, mid)
        except DBMessageNotExistsException:
            raise SanicMessageNotFound('Message not found')

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        response_model = ResponseCreateMessageDto(message)

        return await self.make_response_json(status=200, body=response_model.dump())

    async def method_delete(
            self, request: Request, body: dict, session: DBSession, mid: int, *args, **kwargs
    ) -> BaseHTTPResponse:

        try:
            message = message_queries.delete_message(session, mid)
        except DBMessageNotExistsException:
            raise SanicMessageNotFound('Message not found')

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        return await self.make_response_json(status=204)
