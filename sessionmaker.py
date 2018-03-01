# coding: utf-8

import sys

try:

    from sqlalchemy import create_engine
    from sqlalchemy import Column, Integer, String
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
except:
    sys.exit("Falta biblioteca sqlalchemy!")

engine = create_engine("sqlite:///banco.db")
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)

session = Session()

class Usuario(Base):
    __tablename__ = 'usuarios' # Nome da tabela é usuarios
    id = Column(Integer, primary_key=True)
    nome = Column(String)
l
if __name__ == '__name__':
    Base.metadata.create_all(engine)
    try:
        usuario = Usuario(id=1,nome="Elias Neves")
        session.add(usuario)
        session.commit()
        print("Registro criado")
    except Exception as e:
        print ("Falhou {}".format(e))
