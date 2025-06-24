class JogoService:
    def __init__(self, jogo_repository):
        self.jogo_repository = jogo_repository

    def listar_jogos(self):
        return self.jogo_repository.listar_jogos()

    def buscar_jogo_por_nome(self, nome):
        return self.jogo_repository.buscar_jogo_por_nome(nome)

    def adicionar_jogo(self, nome, descricao, data_lancamento, generos, empresa, preco):
        return self.jogo_repository.adicionar_jogo(nome, descricao, data_lancamento, generos, empresa, preco)

    def adicionar_genero_ao_jogo(self, jogo, genero):
        self.jogo_repository.adicionar_genero_ao_jogo(jogo, genero)

    def listar_generos_do_jogo(self, jogo):
        return self.jogo_repository.listar_generos_do_jogo(jogo)

    def atualizar_jogo(self, nomeJogo, novo_nome, nova_descricao, nova_data, novos_generos, nova_empresa, novo_preco):
        return self.jogo_repository.atualizar_jogo(nomeJogo, novo_nome, nova_descricao, nova_data, novos_generos, nova_empresa, novo_preco)
    
    def remover_jogo(self, nome):
        return self.jogo_repository.remover_jogo(nome)
        