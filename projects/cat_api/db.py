from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("mysql+mysqlconnector://root:password@localhost:3306/Cats")

Base = declarative_base()

Session = sessionmaker(bind=engine)