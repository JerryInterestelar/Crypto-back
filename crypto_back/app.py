from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def get_hell():
    return {'message': 'hello'}
