from typing import Tuple

from configs.config import ApplicationConfig
from context import Context
from transport.sanic import endpoints


def get_routes(config: ApplicationConfig, context: Context) -> Tuple:
    return (
        endpoints.HealthEndpoint(
            config=config, context=context, uri='/', methods=('GET', 'POST'),
        ),
        endpoints.CreateEmployeeEndpoint(
            config, context, uri='/employee', methods=['POST'],
        ),
        endpoints.AuthEmployeeEndpoint(
            config, context, uri='/employee/auth', methods=['POST'],
        ),
        endpoints.EmployeeEndpoint(
            config, context, uri='/employee/<eid:int>', methods=['PATCH', 'DELETE'], auth_required=True,
        ),
        endpoints.AllEmployeeEndpoint(
            config, context, uri='/employee/all', methods=['GET'], auth_required=True,
        ),
        endpoints.CreateMessageEndpoint(
            config, context, uri='/msg', methods=['POST'], auth_required=True,
        ),
        endpoints.MessageEndpoint(
            config, context, uri='/msg/<mid:int>', methods=['PATCH', 'DELETE'], auth_required=True,
        ),
        endpoints.OneMessageEndpoint(
            config, context, uri='/msg/<mid:int>', methods=['GET'], auth_required=True,
        )

    )
