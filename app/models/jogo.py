from peewee import CharField, DateField, IntegerField, Model

from app.config.database import db


class Jogo(Model):
    class Meta:
        database = db
        table_name = 'jogo'
    
    id = IntegerField(primary_key=True)
    nome = CharField(max_length=100, null=False)
    destricao = CharField(max_length=255, null=True)
    data_lancamento = DateField(null=True)
    preco = IntegerField(null=True)
    empresa = CharField(max_length=100, null=True)
   
    def adicionar_genero(self, genero):
        from models.jogo_genero import JogoGenero
        JogoGenero.create(jogo=self, genero=genero)

    def listar_generos(self):
        return [jg.genero for jg in self.generos]