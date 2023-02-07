from typing import Type

import config

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import EmailType


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(EmailType, unique=True, index=True)
    password = Column(String(32), nullable=False)
    registration_time = Column(DateTime, server_default=func.now())

    def __str__(self):
        return self.email


class Adv(Base):
    __tablename__ = 'advertisement'

    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)
    description = Column(String(256))
    creation_time = Column(DateTime, server_default=func.now())
    owner = Column(Integer, ForeignKey('user.id'))

    def __str__(self):
        return self.title


def get_engine():
    return create_engine(config.PG_DSN)


def get_session_maker():
    return sessionmaker(bind=get_engine())


def init_db():
    Base.metadata.create_all(bind=get_engine())


def close_db():
    get_engine().dispose()


ORM_MODEL_CLS = Type[User] | Type[Adv]
ORM_MODEL = User | Adv
