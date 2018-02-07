#!/usr/bin python3
# -*- coding: UTF-8 -*-

try:
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import Column,Integer,String
except:
    sys.exit("Falta complemento - SQLITE!")



engine = create_engine("sqlite:///banco.db")
Base = declarative_base()

class Usuario(Base):
    """docstring for Usuario."""
    __tablename__ = "usuarios"
    id = Column(Integer,primary_key=True)
    nome = Column(String)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
