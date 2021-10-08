from datetime import datetime
from pydantic import BaseModel


''' Model Schema Using Pydantic '''


class User(BaseModel):
    id: int
    username: str
    email: str
    password: str
    register_date: datetime = datetime.utcnow()
