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

    def atualizar(self, nome_antigo, novo_nome):
        genero = self.buscar_por_nome(nome_antigo)
        if not genero:
            raise ValueError(f"Gênero '{nome_antigo}' não encontrado.")
        if self.buscar_por_nome(novo_nome):
            raise ValueError(f"Gênero '{novo_nome}' já existe.")
        if genero.nome == novo_nome:
            raise ValueError(f"Gênero '{novo_nome}' é o mesmo que o atual.")
        if not novo_nome:
            raise ValueError("O novo nome do gênero não pode ser vazio.")
        genero.nome = novo_nome
        genero.save()
        return genero

    def remover(self, generoNome):
        genero = self.buscar_por_nome(generoNome)
        if not genero:
            raise ValueError("Gênero não encontrado.")
        if genero.jogos.exists():
            raise ValueError(f"Gênero '{genero.nome}' não pode ser removido porque está associado a jogos.")
        genero.delete_instance()
        return print(f"Gênero removido com sucesso.")