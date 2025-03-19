from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP, create_engine
from sqlalchemy.orm import sessionmaker
from typing import TypedDict
import logging

from ..config import Config

engine = create_engine(Config.USER_DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'members'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(255), unique=True,nullable=False)
    password = Column(String(255), nullable=False)
    mail = Column(String(255), unique=True, nullable=False)
    created_at = Column(TIMESTAMP)
    last_login_ip = Column(String(45))

class UserData(TypedDict):
    user_name:str
    password:str
    mail:str
    created_at:TIMESTAMP
    last_login_ip:str

class UserDB:
    @staticmethod
    def register_user(register_request:UserData) -> None:
        session = Session()
        try:
            new_user = User(user_name = register_request['user_name'],
                            password = register_request['password'],
                            mail = register_request['mail'],
                            created_at = register_request['created_at'],
                            last_login_ip = register_request['last_login_ip'])
            session.add(new_user)
            session.commit()
        except Exception as e:
            session.rollback()
            logging.error(f'Error occurred: {e}')
        finally:
            session.close()

    @staticmethod
    def query_user(user_name:str) -> User:
        session = Session()
        query_user = session.query(User).filter(User.user_name == user_name).first()
        session.close()
        return query_user
    
    @staticmethod
    def update_user(user_name:str,password:str,mail:str) -> None:
        session = Session()
        try:
            update_user = session.query(User).filter(User.user_name == user_name).first()
            if update_user:
                update_user.password = password
                update_user.mail = mail
            session.commit()
        except Exception as e:
            session.rollback()
            logging.error(f'Error occurred: {e}')
        finally:
            session.close()

    @staticmethod
    def delete_user(user:User) -> None:
        session = Session()
        try:
            session.delete(user)
            session.commit()
        except Exception as e:
            session.rollback()
            logging.error(f'Error occurred: {e}')
        finally:
            session.close()
