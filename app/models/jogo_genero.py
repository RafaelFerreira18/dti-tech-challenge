from peewee import ForeignKeyField, Model

from app.config.database import db
from app.models.genero import Genero
from app.models.jogo import Jogo


class JogoGenero(Model):
    class Meta:
        database = db
        table_name = 'jogo_genero'
    jogo = ForeignKeyField(Jogo, backref="generos")
    genero = ForeignKeyField(Genero, backref="jogos")