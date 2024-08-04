import uvicorn

from enum import Enum

from fastapi import FastAPI
from typing import Optional


app = FastAPI()


class EducationLevel(str, Enum):
    SECONDARY = 'Среднее образование'
    SPECIAL = 'Среднее специальное образование'
    HIGHER = 'Высшее образование'


@app.get('/me')
def hello_author():
    return {'Hello': 'author'}


@app.get('/{name}')
def greetings(
    *,
    surname: str,
    age: Optional[int] = None,
    is_staff: bool = False,
    education_level: Optional[EducationLevel] = None,
    name: str,
) -> dict[str, str]:
    result = ' '.join([name, surname])
    result = result.title()
    if age is not None:
        result += ', ' + str(age)
    if education_level is not None:
        result += ', ' + education_level.lower()
    if is_staff:
        result += ', сотрудник'
    return {'Hello': result}


if __name__ == '__main__':

    try:
        uvicorn.run('main:app', reload=True)
    except KeyboardInterrupt:
        pass
