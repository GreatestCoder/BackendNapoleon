from api.request import RequestCreateEmployeeDto
from db.database import DBSession
from db.exceptions import DBEmployeeExistsException, DBEmployeeNotExistsException
from db.models import DBEmployee


def create_employee(session: DBSession, employee: RequestCreateEmployeeDto, hashed_password: bytes) -> DBEmployee:
    new_employee = DBEmployee(
        login=employee.login,
        password=hashed_password,
        first_name=employee.first_name,
        last_name=employee.last_name,
        position=employee.position,
        department=employee.department,
    )
    if session.get_employee_by_login(new_employee.login) is not None:
        raise DBEmployeeExistsException

    session.add_model(new_employee)

    return new_employee


def get_employee(session: DBSession, login: str = None, employee_id: int = None) -> DBEmployee:
    db_employee = None

    if login is not None:
        db_employee = session.get_employee_by_login(login)
    elif employee_id is not None:
        db_employee = session.get_employee_by_id(employee_id)

    if db_employee is None:
        raise DBEmployeeNotExistsException
    return db_employee
