from config import engine
from config import metadata
from config import app
import uvicorn

from app.route import user_route

app.include_router(user_route, prefix="/app/user", tags=["user"])


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI CRUD Example."}


if __name__ == '__main__':
    metadata.create_all(engine)
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
