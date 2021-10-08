from fastapi import FastAPI
import databases
import sqlalchemy

''' FastAPI CONFIGURATION '''
app = FastAPI(docs_url="/app/v2/docs",
              redoc_url="/app/v2/redocs",
              title="Core API",
              )

''' DATABASE CONNECTION '''
DATABASE_URL = "postgresql://fastapi:user_test@localhost/fastapi"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    DATABASE_URL
)

''' APP EVENT SETTING'''


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
