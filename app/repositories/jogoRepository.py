from app.models.jogo import Jogo
from app.models.jogo_genero import JogoGenero


class JogoRepository:
    
    def listar_jogos():
        return Jogo.select()

    def buscar_jogo_por_id(jogo_id):
        return Jogo.get_or_none(Jogo.id == jogo_id)

    def adicionar_jogo(nome):
        jogo = Jogo.create(nome=nome)
        return jogo

    def adicionar_genero_ao_jogo(jogo, genero):
        JogoGenero.create(jogo=jogo, genero=genero)

    def listar_generos_do_jogo(jogo):
        return jogo.generos
    
    def atualizar_jogo(jogo, novo_nome):
        jogo.nome = novo_nome
        jogo.save()
        return jogo