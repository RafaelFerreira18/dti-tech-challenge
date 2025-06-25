import unittest
from unittest.mock import MagicMock, patch

from app.controllers.generoController import GeneroController
from app.models.genero import Genero


class TestGeneroController(unittest.TestCase):
    def setUp(self):
        self.genero_service = MagicMock()
        self.controller = GeneroController(self.genero_service)

    @patch("builtins.input", return_value="1")
    def test_listar_generos(self, mock_input):
        self.controller.menu()
        self.genero_service.listar_generos.assert_called_once()

    @patch("builtins.input", side_effect=["2", "Ação"])
    @patch("builtins.print")
    def test_buscar_ou_criar_genero(self, mock_print, mock_input):
        genero_mock = Genero(nome="Ação")
        self.genero_service.buscar_ou_criar.return_value = genero_mock

        self.controller.menu()

        self.genero_service.buscar_ou_criar.assert_called_once_with("Ação")
        mock_print.assert_any_call("Gênero encontrado ou criado: Ação")

    @patch("builtins.input", side_effect=["3", "Ação", "Aventura"])
    @patch("builtins.print")
    def test_atualizar_genero_com_sucesso(self, mock_print, mock_input):
        self.controller.menu()

        self.genero_service.atualizar_genero.assert_called_once_with("Ação", "Aventura")
        mock_print.assert_any_call("Gênero atualizado para: Aventura")

    @patch("builtins.input", side_effect=["4", "Terror"])
    @patch("builtins.print")
    def test_remover_genero_com_sucesso(self, mock_print, mock_input):
        self.controller.menu()

        self.genero_service.remover_genero.assert_called_once_with("Terror")
        mock_print.assert_any_call("Gênero 'Terror' removido com sucesso.")

    @patch("builtins.input", return_value="x")
    @patch("builtins.print")
    def test_opcao_invalida(self, mock_print, mock_input):
        self.controller.menu()
        mock_print.assert_any_call("Opção inválida. Tente novamente.")

    @patch("builtins.input", side_effect=["2", ""])
    @patch("builtins.print")
    def test_erro_valor_vazio_ao_buscar_ou_criar(self, mock_print, mock_input):
        self.controller.menu()
        mock_print.assert_any_call("Erro de entrada: Nome do gênero não pode ser vazio.")

if __name__ == "__main__":
    unittest.main()