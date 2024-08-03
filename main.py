import uvicorn

from fastapi import FastAPI
from typing import Optional


app = FastAPI()


@app.get('/me')
def hello_author():
    return {'Hello': 'author'}


@app.get('/{name}')
def greetings(
        name: str,
        surname: str,
        age: Optional[int] = None,
        is_staff: bool = False
) -> dict[str, str]:
    result = ' '.join([name, surname])
    result = result.title()
    if age is not None:
        result += ', ' + str(age)
    if is_staff:
        result += ', сотрудник'
    return {'Hello': result}


@app.get('/multiplication')
def multiplication(
    length: int,
    width: int,
    depth: Optional[int] = None
) -> int:
    result = length * width
    if depth is not None:
        result *= depth
    return result


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
