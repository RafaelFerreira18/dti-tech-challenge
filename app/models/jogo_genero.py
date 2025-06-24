from peewee import CompositeKey, ForeignKeyField, Model

from app.config.database import db
from app.models.genero import Genero
from app.models.jogo import Jogo


class JogoGenero(Model):
    jogo = ForeignKeyField(Jogo, backref="generos")
    genero = ForeignKeyField(Genero, backref="jogos")

    class Meta:
        database = db
        table_name = 'jogo_genero'
        primary_key = CompositeKey('jogo', 'genero')
