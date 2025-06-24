class GeneroService:
    def __init__(self, genero_repository):
        self.genero_repository = genero_repository

    def criar_genero(self, nome):
        return self.genero_repository.criar(nome)

    def buscar_genero_por_nome(self, nome):
        return self.genero_repository.buscar_por_nome(nome)

    def listar_todos_generos(self):
        return self.genero_repository.listar_todos()

    def listar_jogos_por_genero(self, genero):
        return self.genero_repository.listar_jogos(genero)

    def atualizar_genero(self, genero, novo_nome):
        return self.genero_repository.atualizar(genero, novo_nome)