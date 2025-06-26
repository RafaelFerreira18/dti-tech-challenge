from app.models import Genero
from app.utils.logger import logger


class GeneroRepository:
    def criar(self, nome):
        nome = nome.strip()
        if not nome:
            raise ValueError("O nome do gênero não pode ser vazio ou composto apenas por espaços.")

        genero = Genero.create(nome=nome)
        logger.info(f"Gênero '{nome}' criado com sucesso.")
        return genero
    
    def buscar_por_nome(self, nome):
        if not nome:
            logger.error("Nome do gênero não informado.")
            return None

        genero = Genero.get_or_none(Genero.nome == nome)
        
        if genero:
            logger.info(f"Gênero '{nome}' encontrado.")
        else:
            logger.error(f"Gênero '{nome}' não encontrado.")
        
        return genero
    
    def listar_todos(self):
        logger.info("Listando todos os gêneros.")
        return list(Genero.select())

    def listar_jogos(self, genero):
        from models.jogo_genero import JogoGenero
        return [jg.jogo for jg in JogoGenero.select().where(JogoGenero.genero == genero)]

    def atualizar(self, nome_antigo, novo_nome):
        genero = self.buscar_por_nome(nome_antigo)

        if self.buscar_por_nome(novo_nome):
            logger.error(f"Gênero '{novo_nome}' já existe.")
            raise ValueError("Já existe um gênero com esse nome.")

        if genero.nome == novo_nome:
            logger.error(f"Gênero '{novo_nome}' é o mesmo que o atual.")
            raise ValueError("O novo nome é o mesmo que o atual.")

        if not novo_nome:
            logger.error("O novo nome do gênero não pode ser vazio.")
            raise ValueError("O novo nome não pode ser vazio.")

        genero.nome = novo_nome
        genero.save()
        logger.info(f"Gênero atualizado de '{nome_antigo}' para '{novo_nome}'.")
        return genero


    def remover(self, generoNome):
        genero = self.buscar_por_nome(generoNome)
        if not genero:
            logger.error(f"Gênero '{generoNome}' não encontrado para remoção.")
            raise ValueError(f"Gênero '{generoNome}' removido com sucesso.")
        if genero.jogos.exists():
            logger.error(f"Gênero '{genero.nome}' não pode ser removido porque está associado a jogos.")
            raise ValueError(f"Gênero '{genero.nome}' não pode ser removido porque está associado a jogos.")
        genero.delete_instance()
        logger.info(f"Gênero '{generoNome}' removido com sucesso.")
        return print(f"Gênero removido com sucesso.")