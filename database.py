from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

engine = create_engine('sqlite:///task_manager.db')
Session = sessionmaker(bind=engine)
session = Session()

def initialize_db():
    Base.metadata.create_all(engine)
