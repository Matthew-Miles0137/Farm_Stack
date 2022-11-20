



from models import AccountDB
from fastapi.encoders import jsonable_encoder


account = {'user_name':'Matthaeus', 'password':'scorpion', 'first_name':'Matthews'}

adb = AccountDB(**account)

print(jsonable_encoder(adb))