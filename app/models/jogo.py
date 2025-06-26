from peewee import (AutoField, CharField, DateField, FloatField,
                    IntegrityError, Model)

from app.config.database import db


class Jogo(Model):
    class Meta:
        database = db
        table_name = 'jogo'

    id = AutoField() 
    nome = CharField(max_length=100, null=False)
    descricao = CharField(max_length=255, null=True)
    data_lancamento = DateField(null=False)
    preco = FloatField(null=True)
    empresa = CharField(max_length=100, null=True)
   
    def adicionar_genero(self, genero):
        from app.models.jogo_genero import JogoGenero
        try:
            JogoGenero.create(jogo=self, genero=genero)
        except IntegrityError:
            pass 
        

    def listar_generos(self):
        return [jg.genero for jg in self.generos]
    
    def __str__(self):
        try:
            generos_nomes = [genero.nome for genero in self.listar_generos()]
        except Exception:
            generos_nomes = []
        return (f"Nome: {self.nome}, Gêneros: {generos_nomes}, Descrição: {self.descricao}, "
                f"Data de Lançamento: {self.data_lancamento}, Empresa: {self.empresa}, Preço: {self.preco}")

