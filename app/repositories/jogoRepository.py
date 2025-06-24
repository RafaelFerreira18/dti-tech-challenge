from app.models.jogo import Jogo
from app.models.jogo_genero import JogoGenero


class JogoRepository:
    def __init__(self):
        pass
    
    def listar_jogos(self):
        jogos = Jogo.select()
        for jogo in jogos:
            print(jogo)

    def buscar_jogo_por_nome(self, nome):
        jogo = Jogo.get_or_none(Jogo.nome == nome)
        return print(jogo) if jogo else None

    def adicionar_jogo(self, nome, descricao, data_lancamento, generos, empresa, preco):
        jogo = Jogo.create(nome=nome, descricao=descricao, data_lancamento=data_lancamento, empresa=empresa, preco=preco)
        print(generos)
        for genero in generos:
            JogoGenero.create(jogo=jogo, genero=genero)
        print(f"Jogo adicionado: {jogo.nome}")
        return jogo

    def adicionar_genero_ao_jogo(jogo, genero):
        JogoGenero.create(jogo=jogo, genero=genero)

    def listar_generos_do_jogo(jogo):
        return jogo.generos
    
    def atualizar_jogo(self,nomeJogo, novo_nome, nova_descricao, nova_data, novos_generos, nova_empresa, novo_preco):
        jogo = Jogo.get_or_none(Jogo.nome == nomeJogo)
        jogo.nome = novo_nome
        jogo.descricao = nova_descricao
        jogo.data_lancamento = nova_data
        jogo.empresa = nova_empresa
        jogo.preco = novo_preco
        JogoGenero.delete().where(JogoGenero.jogo == jogo).execute()
        for genero in novos_generos:
            JogoGenero.create(jogo=jogo, genero=genero)
        for genero in novos_generos:
            jogo.adicionar_genero(genero)
        
        print(f"Jogo atualizado: {jogo.nome}")
        jogo.save()
        return jogo
    
    def remover_jogo(self, nome):
        jogo = Jogo.get_or_none(Jogo.nome == nome)
        if jogo:
            jogo.delete_instance()
            print(f"Jogo removido com sucesso.")
        else:
            print(f"Jogo não encontrado.")