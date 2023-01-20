from fastapi import FastAPI

app = FastAPI()

# creamos una operacion e indicamos el endpoint

# @app.get: decorador para el endpoint
# async: siempre que se llame a un servidor, la funcion debe ser asincrona
@app.get("/")
async def root():
    return "¡Hola Mundo, desde FastAPI!"

# si llamamos a la misma funcion en el mismo path, aparece la primera
# por ende cambiamos el path
# y tambien el nombre de la funcion
@app.get("/user/{name}")
async def user(name: str):
    return { "Name": name,
        "Lastname": "Da Silva" }
