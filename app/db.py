from core.config import settings
from sqlalchemy import create_engine, MetaData, Column, String, Date, Table, Integer


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
metadata = MetaData()

# Exemplo com SQLAlchemy
'''

users = Table(
    'usuario',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    Colum('nome', String, nullable=False),
    Column('email', String, nullable=False),
    Column('password', String, nullable=False)

)

'''
