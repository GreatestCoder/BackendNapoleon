from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request import RequestCreateMessageDto
from api.response import ResponseCreateMessageDto
from transport.sanic.endpoints import BaseEndpoint

from db.queries import message as message_queries


class CreateMessageEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestCreateMessageDto(body)

        sender_id = body.get('eid')

        db_messages = message_queries.create_message(session, request_model, sender_id)
        session.commit_session()

        response_model = ResponseCreateMessageDto(db_messages)

        return await self.make_response_json(body=response_model.dump(), status=201)
