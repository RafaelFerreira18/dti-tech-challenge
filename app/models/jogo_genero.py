from peewee import ForeignKeyField, Model

from app.models.genero import Genero
from app.models.jogo import Jogo


class JogoGenero(Model):
    jogo = ForeignKeyField(Jogo, backref="generos")
    genero = ForeignKeyField(Genero, backref="jogos")