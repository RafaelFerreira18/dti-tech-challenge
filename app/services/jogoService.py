class JogoService:
    def __init__(self, jogo_repository):
        self.jogo_repository = jogo_repository

    def listar_jogos(self):
        return self.jogo_repository.listar_jogos()

    def buscar_jogo_por_id(self, jogo_id):
        return self.jogo_repository.buscar_jogo_por_id(jogo_id)

    def adicionar_jogo(self, nome):
        return self.jogo_repository.adicionar_jogo(nome)

    def adicionar_genero_ao_jogo(self, jogo, genero):
        self.jogo_repository.adicionar_genero_ao_jogo(jogo, genero)

    def listar_generos_do_jogo(self, jogo):
        return self.jogo_repository.listar_generos_do_jogo(jogo)

    def atualizar_jogo(self, jogo, novo_nome):
        return self.jogo_repository.atualizar_jogo(jogo, novo_nome)