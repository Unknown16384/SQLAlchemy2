from session import Connection
from main import Products
from pydantic import BaseModel

class ODT(BaseModel):
    Name: str
    Amount: int

connect = Connection(sql_type='SQLite', db_name='mydb')
engine = connect.engine
session = connect.session

for row in session.query(Products).all():
    print(ODT.model_validate(row, from_attributes=True))
