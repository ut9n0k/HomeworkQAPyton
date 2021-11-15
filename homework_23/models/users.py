from sqlalchemy import VARCHAR, Integer, Column
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__ = "users"
    id = Column(VARCHAR(8), primary_key=True)
    name = Column(VARCHAR(25))
    email = Column(VARCHAR(30))
    age = Column(Integer)

    def __str__(self):
        return f"\n{self.id}\n{self.name}\n{self.email}\n{self.age}"
