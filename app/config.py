import os
basedir = os.path.abspath(os.path.dirname(__name__))
print(basedir)
db_info = {'host': 'localhost',
           'database': 'mati',
           'user': 'postgres',
           'password': '1234',
           'port': ''}
class Config:
    SQLALCHEMY_DATABASE_URI = f"postgresql:///{db_info['user']}:{db_info['password']}@{db_info['host']}/{db_info['database']}"

