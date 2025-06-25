class GeneroService:
    def __init__(self, genero_repository):
        self.genero_repository = genero_repository

    def buscar_ou_criar(self, nome):
        genero = self.genero_repository.buscar_por_nome(nome)
        if not genero:
            genero = self.genero_repository.criar(nome)
        return genero

    def listar_generos(self):
        generos = self.genero_repository.listar_todos()
        if not generos:
            print("Nenhum gênero encontrado.")
        for genero in generos:
            print(genero.nome)

    def listar_jogos_por_genero(self, genero):
        print(f"Listando jogos do gênero: {genero.nome}")
        return self.genero_repository.listar_jogos(genero)

    def atualizar_genero(self, nome_antigo, novo_nome):
        genero = self.genero_repository.buscar_por_nome(nome_antigo)
        if not genero:
            raise ValueError("Gênero não encontrado para atualizar.")
        if self.genero_repository.buscar_por_nome(novo_nome):
            raise ValueError("Já existe um gênero com esse nome.")
        return self.genero_repository.atualizar(genero, novo_nome)

    def remover_genero(self, nome):
        genero = self.genero_repository.buscar_por_nome(nome)
        if not genero:
            raise ValueError("Gênero não encontrado para remoção.")
        return self.genero_repository.remover(nome)
