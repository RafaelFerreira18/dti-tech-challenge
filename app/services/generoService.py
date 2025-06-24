class GeneroService:
    def __init__(self, genero_repository):
        self.genero_repository = genero_repository

    def buscar_ou_criar(self, nome):
        genero = self.genero_repository.buscar_por_nome(nome)
        if not genero:
            genero = self.genero_repository.criar(nome)
        return print(genero.nome)

    def listar_generos(self):
        generos = self.genero_repository.listar_todos()
        for genero in generos:
            print(genero.nome)

    def listar_jogos_por_genero(self, genero):
        print(f"Listando jogos do gênero: {genero.nome}")
        return self.genero_repository.listar_jogos(genero)

    def atualizar_genero(self, genero, novo_nome):
        return self.genero_repository.atualizar(genero, novo_nome)
    
    def remover_genero(self, generoNome):
        return self.genero_repository.remover(generoNome)