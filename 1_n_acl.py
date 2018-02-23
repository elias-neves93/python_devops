import sys

try:
    from sqlalchemy import create_engine
    from sqlalchemy import Column,Integer,String,ForeignKey
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker, relationship

except:
    sys.exit("Install the libs!!")

engine = create_engine("sqlite:///banco1.db")
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)

session = Session()

class Funcionario(Base):
    __tablename__ = "funcionarios"
    id = Column(Integer,primary_key=True)
    nome = Column(String)
    depedentes = relationship("Dependentes")

class Dependentes(Base):
    __tablename__ = "dependentes"
    id = Column(Integer,primary_key=True)
    nome = Column(String)
    funcionario_id = Column(Integer,ForeignKey("funcionarios.id"))

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    try:
        funcionario = Funcionario(id=1,nome="Elias Neves")
        session.add(funcionario)
        dependente1 = Dependentes(id=1,nome="Joao")
        dependente2 = Dependentes(id=2,nome="Maria")
        funcionario.dependentes.append(dependente1)
        funcionario.dependentes.append(dependente2)
        session.add(dependente1)
        session.add(dependente2)
        session.commit()
    except Exception as e:
        print ("Falhou {}".format(e))
        print ("Fazendo o rollback")
        session.rollback()
