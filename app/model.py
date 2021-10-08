import sqlalchemy
from config import metadata
from datetime import datetime


''' SQLAlchemy Model'''
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String(50), unique=True),
    sqlalchemy.Column("email", sqlalchemy.String(100), unique=True),
    sqlalchemy.Column("password", sqlalchemy.String(100), unique=True),
    sqlalchemy.Column("register_date", sqlalchemy.DateTime, default=datetime.utcnow().strftime("%Y-%m-%d" "%H:%M:%S"))
)
