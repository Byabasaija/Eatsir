from app.db.config import session
from app.models import User

class Users:
    def __init__(self, id, user_name, first_name, last_name, age, gender, country,status, password,):
        self.id = id
        self.user_name = user_name
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.age = age
        self.gender = gender
        self.status = status

    def create_user(self):
        new_user = User(
            user_id=self.id,
            user_name=self.user_name,
            password= self.password,
            first_name=self.first_name,
            last_name=self.last_name,
            age = self.age,
            gender = self.gender,
            status = self.status,
            country = self.country
        )
        session.add(new_user)
        session.commit()

    @classmethod
    def get_user(cls, user_name, password):
    
        user = session.query(User).filter_by(user_name=user_name, password=password).first()
    
        if user:
            user_dict = user.as_dict()
            return user_dict
        else:
            return None
    

