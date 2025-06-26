from app.models.jogo import Jogo
from app.models.jogo_genero import JogoGenero
from app.utils.logger import logger


class JogoRepository:
    def __init__(self):
        pass
    
    def listar_jogos(self):
        logger.info("Listando todos os jogos.")
        jogos = Jogo.select()
        for jogo in jogos:
            print(jogo)

    def buscar_jogo_por_nome(self, nome):
        jogo = Jogo.get_or_none(Jogo.nome == nome)
        if not jogo:
            logger.error(f"Jogo '{nome}' não encontrado.")
            raise ValueError(f"Jogo não encontrado.")
        logger.info(f"Jogo encontrado: {jogo.nome}")
        return jogo
    
    def adicionar_jogo(self, nome, descricao, data_lancamento, generos, empresa, preco):
        jogo = Jogo.create(nome=nome, descricao=descricao, data_lancamento=data_lancamento, empresa=empresa, preco=preco)
        logger.info(f"Adicionando jogo: {jogo.nome}")
        for genero in generos:
            JogoGenero.create(jogo=jogo, genero=genero)
        print(f"Jogo adicionado: {jogo.nome}")
        return jogo

    def adicionar_genero_ao_jogo(jogo, genero):
        JogoGenero.create(jogo=jogo, genero=genero)
        logger.info(f"Gênero '{genero.nome}' adicionado ao jogo '{jogo.nome}'.")

    def listar_generos_do_jogo(jogo):
        return jogo.generos
    
    def atualizar_jogo(self,nomeJogo, novo_nome, nova_descricao, nova_data, novos_generos, nova_empresa, novo_preco):
        jogo = Jogo.get_or_none(Jogo.nome == nomeJogo)
        if not jogo:
            logger.error(f"Jogo '{nomeJogo}' nao encontrado para atualizaçao.")
        jogo.nome = novo_nome
        if not novo_nome:
            logger.error("Nome do jogo nao pode ser vazio.")
        jogo.descricao = nova_descricao
        if not nova_data:
            logger.error("Data de lançamento nao pode ser vazia.")
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
        logger.info(f"Jogo atualizado de '{nomeJogo}' para '{novo_nome}'.")
        return jogo
    
    def remover_jogo(self, nome):
        jogo = Jogo.get_or_none(Jogo.nome == nome)            
        if jogo:
            jogo.delete_instance()
            print(f"Jogo removido com sucesso.")
            logger.info(f"Jogo '{nome}' removido com sucesso.")
        else:
            print(f"Jogo não encontrado.")
            logger.error(f"Jogo '{nome}' nao encontrado para remoçao.")