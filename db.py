# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


engine = create_engine('mysql+mysqldb://root@localhost:3306/blog?charset=utf8')


Base = declarative_base()

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(64), nullable=False, index = True)
  password = Column(String(64), nullable=False)
  email = Column(String(64), nullable=False, index=True)
  articles = relationship('Article')  

  def __repr__(self):
    return '%s(%r)' %(self.__class__.__name__, self.username)


class Article(Base):
  __tablename__ = 'articles'
  
  id = Column(Integer, primary_key=True)


Base.metadata.create_all(engine)


print(engine)

