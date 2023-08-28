from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    status = Column(String(20), nullable=False)
    gender = Column(String(10), nullable=False)
    country = Column(String(50), nullable=False)
    def as_dict(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'status': self.status,
            'gender': self.gender,
            'country': self.country
        }
