from peewee import CharField, Model

from app.config.database import db


class Genero(Model):
    class Meta:
        database = db
        table_name = 'genero'
    nome = CharField(unique=True)

    def listar_jogos(self):
        return [jg.jogo for jg in self.jogos]