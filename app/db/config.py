from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_NAME = 'eatsir'
DB_USER = 'postgres'
DB_PASSWORD = 'password1'
DB_HOST = 'localhost'
DB_PORT = '5432'

# Create the engine
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Create the session
Session = sessionmaker(bind=engine)
session = Session()

