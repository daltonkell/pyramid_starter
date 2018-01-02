from sqlalchemy import create_engine
from sqlalchemy import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import configure_mappers

from pyramid_starter.database.initializedb import User # import User class

engine = create_engine('sqlite:///:memory', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)


if __name__ == '__main__':
    # create all tables present within MetaData (constructed simultaneouly with
    # User)
    Base.metadata.create_all(engine)
    # create admin entry into User table
    admin = User(username='admin', fullname='Administrator',
                 password='admin')
                 # add the admin entry to the User table 
    Session.add(admin)
