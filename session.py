from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Connection:
    def __init__(self, sql_type, **args):
        if sql_type == 'SQLite': self._eng = create_engine(f'sqlite:///{args['db_name']}.db')
        elif sql_type == 'PostgreSQL': self._eng = create_engine(f'postgresql://{args['user']}:{args['password']}@{args['server']}:{str(args['port'])}/{args['db_name']}')
    @property
    def engine(self): return self._eng
    @property
    def session(self): return sessionmaker(self._eng)()

''' sample:
# connect = Connection('PostgreSQL', server='localhost', port=5433, user='postgres', password='', db_name='database')
connect = Connection(sql_type='SQLite', db_name='mydb')
engine = connect.engine
session = connect.session
'''