class JogoService:
    def __init__(self, jogo_repository):
        self.jogo_repository = jogo_repository

    def listar_jogos(self):
        return self.jogo_repository.listar_jogos()

    def buscar_jogo_por_nome(self, nome):
        return self.jogo_repository.buscar_jogo_por_nome(nome)
        
    def adicionar_jogo(self, nome, descricao, data, generos, empresa, preco):
        if self.jogo_repository.buscar_jogo_por_nome(nome):
            raise ValueError("Já existe um jogo com esse nome.")
        return self.jogo_repository.adicionar_jogo(nome, descricao, data, generos, empresa, preco)

    def atualizar_jogo(self, nome_antigo, novo_nome, descricao, data, generos, empresa, preco):
        jogo = self.jogo_repository.buscar_jogo_por_nome(nome_antigo)
        if not jogo:
            raise ValueError("Jogo a ser atualizado não foi encontrado.")
        return self.jogo_repository.atualizar_jogo(nome_antigo, novo_nome, descricao, data, generos, empresa, preco)

    def remover_jogo(self, nome):
        jogo = self.jogo_repository.buscar_jogo_por_nome(nome)
        if not jogo:
            raise ValueError("Jogo não encontrado.")
        return self.jogo_repository.remover_jogo(nome)
