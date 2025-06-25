import unittest
from unittest.mock import MagicMock

from app.models import Genero, Jogo
from app.services.jogoService import JogoService


class TestJogoService(unittest.TestCase):
    def setUp(self):
        self.jogo_repository = MagicMock()
        self.jogo_service = JogoService(self.jogo_repository)

    def test_adicionar_jogo_com_sucesso(self):
        nome = "God of War"
        descricao = "Ação e mitologia"
        data = "2022-10-20"
        empresa = "Santa Monica Studio"
        preco = 199.99
        generos = [Genero(nome="Ação")]

        self.jogo_repository.buscar_jogo_por_nome.return_value = None

        self.jogo_repository.adicionar_jogo.return_value = Jogo(
            nome=nome,
            descricao=descricao,
            data_lancamento=data,
            empresa=empresa,
            preco=preco
        )

        jogo_criado = self.jogo_service.adicionar_jogo(nome, descricao, data, generos, empresa, preco)

        self.jogo_repository.buscar_jogo_por_nome.assert_called_once_with(nome)
        self.jogo_repository.adicionar_jogo.assert_called_once_with(nome, descricao, data, generos, empresa, preco)
        self.assertEqual(jogo_criado.nome, nome)

    def test_adicionar_jogo_existente(self):
        nome = "God of War"
        self.jogo_repository.buscar_jogo_por_nome.return_value = Jogo(nome=nome)

        with self.assertRaises(ValueError) as context:
            self.jogo_service.adicionar_jogo(nome, "", "", [], "", 0)

        self.assertEqual(str(context.exception), "Já existe um jogo com esse nome.")

    def test_buscar_jogo_por_nome(self):
        nome = "God of War"
        jogo_mock = Jogo(nome=nome)
        self.jogo_repository.buscar_jogo_por_nome.return_value = jogo_mock

        jogo_encontrado = self.jogo_service.buscar_jogo_por_nome(nome)

        self.jogo_repository.buscar_jogo_por_nome.assert_called_once_with(nome)
        self.assertEqual(jogo_encontrado.nome, nome)
    
    def test_buscar_jogo_por_nome_inexistente(self):
        nome = "God of War"
        self.jogo_repository.buscar_jogo_por_nome.return_value = None

        with self.assertRaises(ValueError) as context:
            self.jogo_service.buscar_jogo_por_nome(nome)

        self.assertEqual(str(context.exception), "Jogo não encontrado.")
    
    def test_atualizar_jogo_com_sucesso(self):
        nome_antigo = "God of War"
        novo_nome = "God of War: Ragnarok"
        nova_descricao = "Continuação da saga"
        nova_data = "2022-11-09"
        nova_empresa = "Santa Monica Studio"
        novo_preco = 249.99
        generos = [Genero(nome="Ação")]

        jogo_mock = Jogo(nome=nome_antigo)
        self.jogo_repository.buscar_jogo_por_nome.return_value = jogo_mock

        self.jogo_repository.atualizar_jogo.return_value = Jogo(
            nome=novo_nome,
            descricao=nova_descricao,
            data_lancamento=nova_data,
            empresa=nova_empresa,
            preco=novo_preco
        )

        jogo_atualizado = self.jogo_service.atualizar_jogo(
            nome_antigo, novo_nome, nova_descricao, nova_data, generos, nova_empresa, novo_preco
        )

        self.jogo_repository.buscar_jogo_por_nome.assert_called_once_with(nome_antigo)
        self.jogo_repository.atualizar_jogo.assert_called_once_with(
            nome_antigo, novo_nome, nova_descricao, nova_data, generos, nova_empresa, novo_preco
        )
        self.assertEqual(jogo_atualizado.nome, novo_nome)

    def test_atualizar_jogo_inexistente(self):
        nome_antigo = "God of War"
        novo_nome = "God of War: Ragnarok"

        self.jogo_repository.buscar_jogo_por_nome.return_value = None

        with self.assertRaises(ValueError) as context:
            self.jogo_service.atualizar_jogo(nome_antigo, novo_nome, "", "", [], "", 0)

        self.assertEqual(str(context.exception), "Jogo a ser atualizado não foi encontrado.")
    
    def test_remover_jogo_com_sucesso(self):
        nome = "God of War"
        jogo_mock = Jogo(nome=nome)
        self.jogo_repository.buscar_jogo_por_nome.return_value = jogo_mock

        self.jogo_service.remover_jogo(nome)

        self.jogo_repository.buscar_jogo_por_nome.assert_called_once_with(nome)
        self.jogo_repository.remover_jogo.assert_called_once_with(nome)
    
    def test_remover_jogo_inexistente(self):
        nome = "God of War"
        self.jogo_repository.buscar_jogo_por_nome.return_value = None

        with self.assertRaises(ValueError) as context:
            self.jogo_service.remover_jogo(nome)

        self.assertEqual(str(context.exception), "Jogo não encontrado.")
    

if __name__ == "__main__":
    unittest.main()
