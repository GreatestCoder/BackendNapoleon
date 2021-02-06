from marshmallow import Schema, fields

from api.base import RequestDto


class RequestCreateMessageDtoSchema(Schema):
    sender_id = fields.Int(required=True, allow_none=False)
    message = fields.Str(required=True, allow_none=False)
    recipient_id = fields.Int(required=True, allow_none=False)


class RequestCreateMessageDto(RequestDto, RequestCreateMessageDtoSchema):
    __schema__ = RequestCreateMessageDtoSchema
