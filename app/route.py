from fastapi import APIRouter
from typing import List
from config import database

from passlib.context import CryptContext

from .model import users
from .schema import User

user_route = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@user_route.get("/users", response_model=List[User], status_code=200)
async def all_users():
    query = users.select()
    all_users = await database.fetch_all(query)
    if users is None:
        return {"message": " No users found!"}
    else:
        return all_users


@user_route.get("/user/{id}", response_model=User, status_code=200)
async def get_post(id: int):
    query = users.select().where(users.c.id == id)
    return await database.fetch_one(query=query)


@user_route.post("/create/", response_model=User, status_code=201)
async def create_user(user: User):
    query = users.insert().values(username=user.username, email=user.email, password=pwd_context.hash(user.password),
                                  register_date=user.register_date)
    last_record_id = await database.execute(query=query)
    return {**user.dict(), "id": last_record_id}


@user_route.patch("/update/{id}", response_model=User)
async def update(id: int, user: User):
    query = users.update().where(users.c.id == id).values(username=user.username, email=user.email,
                                                          password=pwd_context.hash(user.password),
                                                          register_date=user.register_date)
    last_record_id = await database.execute(query=query)
    return {**user.dict(), "id": last_record_id}


@user_route.delete("/delete/{id}", response_model=User)
async def delete(id: int):
    query = users.delete().where(users.c.id == id)
    await database.execute(query)
    return {
        "status": True,
        "message": "This user deleted successfully."
    }
