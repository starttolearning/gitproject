# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Table


engine = create_engine('mysql+mysqldb://root@localhost:3306/blog?charset=utf8')


Base = declarative_base()

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(64), nullable=False, index = True)
  password = Column(String(64), nullable=False)
  email = Column(String(64), nullable=False, index=True)
  articles = relationship('Article')  
  userinfo = relationship('UserInfo', backref='user', uselist=False)


  def __repr__(self):
    return '%s(%r)' %(self.__class__.__name__, self.username)


class Article(Base):
  __tablename__ = 'articles'
  
  id = Column(Integer, primary_key=True)
  title = Column(String(255), nullabel=False, index=True)
  content = Column(Text)
  user_id = Column(Integer, ForeignKey('users.id'))
  author = relationship('User')

  def __repr__(self):
    return '%s(%r)' %(self.__class__.__name__, self.title)
print(engine)

class UserInfo(Base):
  __tablename__ = 'userinfos'

  id = Column(Integer, primary_key=True)
  name = Column(String(64))
  qq = Column(String(11))
  phone = Column(String(11))
  link = Column(String(64))
  user_id = Column(Integer, ForeignKey('users.id'))

article_tag = Table(
  'article_tag', Base.metadata,
  Column('article_id', Integer, ForeignKey('articles.id')),
  Column('tag_id', Integer, ForeignKey('tags_id'))
)

class Tag(Base):
  __tablename__ = 'tags'
  id = Column(Integer, primary_key=True)
  name = Column(String(64), nullable=False, index=True)

  def __repr__(self):
    return '%s(%r)' %(self.__class__.__name__, self.name)


if __name__ == '__main__':
  Base.metadata.create_all(engine)



