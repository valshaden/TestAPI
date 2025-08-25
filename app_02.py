from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World-2"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"ты ввел = ": item_id, "q": q}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"ты ввел = ": item_id, "q": q}

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
