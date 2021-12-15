from fastapi import FastAPI

app = FastAPI(title='serv')

@app.get("/")
async def root():
    return {"message": "Hello World"}
