from decouple import config
DB_URL = config('DB_URL', cast=str)
DB_NAME = config('DB_NAME', cast=str)
COLLECTION_NAME = "accounts1"


# running this file will print the values stored in the .env file
#print(DB_NAME, COLLECTION_NAME, DB_URL)


from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from routers.accounts import router as accounts_router

app = FastAPI()
app.include_router(accounts_router, prefix="/accounts", tags=["accounts"])




@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(DB_URL)
    app.mongodb = app.mongodb_client[DB_NAME]
@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()