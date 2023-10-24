from fastapi import FastAPI, Request, status
from pydantic import BaseModel
import uvicorn

app = FastAPI()
class Article(BaseModel):
    title: str

@app.get("/from_path/{math}")
def search_by_path(request: Request, math: str):
    for math in math.split():
        if math != "":
            try:
                math = math.replace(':', '/')
                data = eval(math)
                return data, status.HTTP_200_OK
            except ZeroDivisionError:
                data = "error 0"
                return data, status.HTTP_200_OK
            except:
                data = "error"
                return data, status.HTTP_200_OK