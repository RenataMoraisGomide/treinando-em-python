import sqlalchemy as sqlA
import pymongo
from requests import Session
from rich import inspect
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, create_engine
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"
    #atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"


class Address(Base):
    __tablename__ = "Address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(40), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship("User", back_populates="Address")

    def __repr__(self):
        return f"Address (id={self.id}, email={self.email_address})"


print(User.__tablename__)


#conexão com banco de dados
engine = create_engine("sqlite://")

#criando as classes como tabela no banco de dados;
Base.metadata.create_all(engine)

inspetor_engine = inspect(engine)

print(inspetor_engine.has_table("user_account"))

print(inspetor_engine.get_table_names())

with Session(engine) as session:
    renata = User(
        nome = "renata",
        fullname="Renata Morais",
        address=[Address(email_address = 'renatamoraisgomide@gmail.com')]
    )



    #enviando para o Banco de dados
    session.add_all([renata])

session.comit()






