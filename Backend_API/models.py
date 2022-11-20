

from bson import ObjectId
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

from pydantic import BaseModel, Field
from typing import Optional




class MongoBaseModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

class Config:
    json_encoders = {ObjectId: str}


class AccountBase(MongoBaseModel):   
    user_name: str = Field(..., min_length=8)
    password: str = Field(..., min_length=8)
    first_name: str = Field(..., min_length=8)

class AccountUpdate(MongoBaseModel):    
    password: Optional[str] = None
class AccountDB(AccountBase):
    pass



