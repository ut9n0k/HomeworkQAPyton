from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine("postgresql://postgres:123@localhost/mydb")

__session = sessionmaker(engine)
session: Session = __session()
