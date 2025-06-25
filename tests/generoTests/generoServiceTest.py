import unittest
from unittest.mock import MagicMock

from app.models.genero import Genero
from app.services.generoService import GeneroService


class TestGeneroService(unittest.TestCase):
    def setUp(self):
        self.genero_repository = MagicMock()
        self.genero_service = GeneroService(self.genero_repository)

    def test_buscar_ou_criar_existente(self):
        genero_mock = Genero(nome="Ação")
        self.genero_repository.buscar_por_nome.return_value = genero_mock

        resultado = self.genero_service.buscar_ou_criar("Ação")

        self.genero_repository.buscar_por_nome.assert_called_once_with("Ação")
        self.assertEqual(resultado.nome, genero_mock.nome)

    def test_buscar_ou_criar_novo(self):
        self.genero_repository.buscar_por_nome.return_value = None
        genero_mock = Genero(nome="Aventura")
        self.genero_repository.criar.return_value = genero_mock

        resultado = self.genero_service.buscar_ou_criar("Aventura")

        self.genero_repository.buscar_por_nome.assert_called_once_with("Aventura")
        self.genero_repository.criar.assert_called_once_with("Aventura")
        self.assertEqual(resultado.nome, genero_mock.nome)

    def test_listar_generos_com_resultados(self):
        generos = [Genero(nome="Ação"), Genero(nome="Terror")]
        self.genero_repository.listar_todos.return_value = generos

        with unittest.mock.patch("builtins.print") as mock_print:
            self.genero_service.listar_generos()

        mock_print.assert_any_call("Ação")
        mock_print.assert_any_call("Terror")

    def test_listar_generos_vazio(self):
        self.genero_repository.listar_todos.return_value = []

        with unittest.mock.patch("builtins.print") as mock_print:
            self.genero_service.listar_generos()

        mock_print.assert_any_call("Nenhum gênero encontrado.")

    def test_listar_jogos_por_genero(self):
        genero = Genero(nome="RPG")
        self.genero_repository.listar_jogos.return_value = ["Jogo1", "Jogo2"]

        with unittest.mock.patch("builtins.print") as mock_print:
            jogos = self.genero_service.listar_jogos_por_genero(genero)

        self.assertEqual(jogos, ["Jogo1", "Jogo2"])
        mock_print.assert_called_once_with("Listando jogos do gênero: RPG")

    def test_atualizar_genero_com_sucesso(self):
        genero_antigo = Genero(nome="Indie")
        self.genero_repository.buscar_por_nome.side_effect = [genero_antigo, None]

        self.genero_service.atualizar_genero("Indie", "Independente")

        self.genero_repository.atualizar.assert_called_once_with(genero_antigo, "Independente")

    def test_atualizar_genero_nao_encontrado(self):
        self.genero_repository.buscar_por_nome.return_value = None

        with self.assertRaises(ValueError) as context:
            self.genero_service.atualizar_genero("Inexistente", "Novo")

        self.assertEqual(str(context.exception), "Gênero não encontrado para atualizar.")

    def test_atualizar_genero_com_nome_duplicado(self):
        genero_existente = Genero(nome="Ação")
        self.genero_repository.buscar_por_nome.side_effect = [genero_existente, genero_existente]

        with self.assertRaises(ValueError) as context:
            self.genero_service.atualizar_genero("Ação", "Ação")

        self.assertEqual(str(context.exception), "Já existe um gênero com esse nome.")

    def test_remover_genero_com_sucesso(self):
        genero = Genero(nome="Estratégia")
        self.genero_repository.buscar_por_nome.return_value = genero

        self.genero_service.remover_genero("Estratégia")

        self.genero_repository.remover.assert_called_once_with("Estratégia")

    def test_remover_genero_nao_encontrado(self):
        self.genero_repository.buscar_por_nome.return_value = None

        with self.assertRaises(ValueError) as context:
            self.genero_service.remover_genero("Fantasia")

        self.assertEqual(str(context.exception), "Gênero não encontrado para remoção.")


if __name__ == "__main__":
    unittest.main()
