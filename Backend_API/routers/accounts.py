from fastapi import APIRouter, Request, Body, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models import AccountBase, AccountDB
from urllib.error import HTTPError
from typing import Optional, List
from werkzeug.exceptions import HTTPException, NotFound

router = APIRouter()

@router.get("/", response_description="List all accounts")
async def list_accounts(request: Request):
    accounts = await request.app.mongodb["accounts1"].find().to_list(1000)
    return accounts
    

@router.get("/{id}", response_description="Get a single account")
async def show_account(id: str, request: Request):
    if (account := await request.app.mongodb
      ["accounts1"].find_one({"_id": id})) is not None:
        return AccountDB(**account)
    raise HTTPException(f"Account with {id} not found", status.HTTP_404_NOT_FOUND)


@router.post("/", response_description="Add new account")
async def create_account(request: Request, account: AccountBase = Body(...)):
    account = jsonable_encoder(account)
    # account1 is the database to which the new account will be added.
    new_account = await request.app.mongodb["accounts1"].insert_one(account)
    created_account = await request.app.mongodb["accounts1"].find_one(
        {"_id": new_account.inserted_id}
    )
    return JSONResponse(status_code=status.HTTP_201_CREATED, 
        content=created_account)