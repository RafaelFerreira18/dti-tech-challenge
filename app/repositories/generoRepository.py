from app.models import Genero


class GeneroRepository:
    def criar(self, nome):
        return Genero.create(nome=nome)
    
    def buscar_por_nome(self, nome):
        return Genero.get_or_none(Genero.nome == nome)
    
    def listar_todos(self):
        return list(Genero.select())

    def listar_jogos(self, genero):
        from models.jogo_genero import JogoGenero
        return [jg.jogo for jg in JogoGenero.select().where(JogoGenero.genero == genero)]

    def atualizar(self, genero, novo_nome):
        genero.nome = novo_nome
        genero.save()
        return genero