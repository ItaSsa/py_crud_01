from sqlalchemy import create_engine

# conn SQLite in memory
engine = create_engine('sqlite:///mydb.db', echo=True)

print("Connection successfully.")

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# create table
Base.metadata.create_all(engine)

# from sqlalchemy.orm import sessionmaker

# Session = sessionmaker(bind=engine)
# session = Session()

# new_user = User(name='João', age=28)
# session.add(new_user)
# session.commit()

# print("User inserted")

# user = session.query(User).filter_by(name='João').first()
# print(f"Found user: {user.name}, age: {user.age}")



# from sqlalchemy.orm import sessionmaker
# # as the engine is ready

# Session = sessionmaker(bind=engine)
# session = Session()

# try:
#     new_user = User(name='Ana', age=25)
#     session.add(new_user)
#     session.commit()
# except:
#     session.rollback()
#     raise
# finally:
#     session.close()

# from sqlalchemy.orm import sessionmaker
# # as the engine is ready

# Session = sessionmaker(bind=engine)
# session = Session()

# user = session.query(User).filter_by(name='Ana').first()
# print(f"Found user: {user.name}, age: {user.age}")


from sqlalchemy.orm import sessionmaker, Session
# as the engine is ready

Session = sessionmaker(bind=engine)

with Session.begin() as session:
    new_user = User(name='Tiaha', age=25)
    session.add(new_user)
#     # The commit is done automatically here if no exceptions occur
#     # The rollback is automatically called if an exception occurs
#     # The session is automatically closed when exiting the with block

with Session() as session:
    user = session.query(User).filter_by(name='Tiaha').first()
    print(f"Found user: {user.name}, age: {user.age}")
    # print(user)