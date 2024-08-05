import uvicorn

from fastapi import Body, FastAPI

from schemas import Person


app = FastAPI()


@app.post('/hello')
def greetings(
        person: Person = Body(
            ..., openapi_examples=Person.Config.schema_extra['examples']
        )
) -> dict[str, str]:
    if isinstance(person.surname, list):
        surnames = ' '.join(person.surname)
    else:
        surnames = person.surname
    result = ' '.join([person.name, surnames])
    result = result.title()
    if person.age is not None:
        result += ', ' + str(person.age)
    if person.education_level is not None:
        result += ', ' + person.education_level.lower()
    if person.is_staff:
        result += ', сотрудник'
    return {'Hello': result}


if __name__ == '__main__':

    try:
        uvicorn.run('main:app', reload=True)
    except KeyboardInterrupt:
        pass
