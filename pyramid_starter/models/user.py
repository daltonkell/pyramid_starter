from sqlalchemy import Column, String, Integer
from sqlalchemy import declarative_base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<username='%s', fullname='%s', password='%s')>" % (self.name,
                self.fullname, self.password)
