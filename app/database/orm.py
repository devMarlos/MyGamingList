from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Configuração do Banco de Dados
engine = create_engine("sqlite:///app/database/games.db", echo=False)
Base = declarative_base()

class Game(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    plataforma = Column(String, nullable=False)
    nota = Column(Float, nullable=False)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Função para adicionar um jogo
def adiciona_games(nome, ano, nota, plataforma):
    session = Session()
    game = Game(nome=nome, ano=ano, nota=nota, plataforma=plataforma)
    session.add(game)
    session.commit()
    session.close()

# Função para atualizar um jogo
def atualiza_game(id, nome=None, ano=None, nota=None, plataforma=None):
    session = Session()
    game = session.query(Game).filter_by(id=id).first()
    if game:
        if nome:
            game.nome = nome
        if ano:
            game.ano = ano
        if nota:
            game.nota = nota
        if plataforma:
            game.plataforma = plataforma
        session.commit()
    session.close()

# Função para listar todos os jogos
def listar_games():
    session = Session()
    games = session.query(Game).all()
    session.close()
    return games

# Função para excluir um jogo
def excluir_game(id):
    session = Session()
    game = session.query(Game).filter_by(id=id).first()
    if game:
        session.delete(game)
        session.commit()
    session.close()
