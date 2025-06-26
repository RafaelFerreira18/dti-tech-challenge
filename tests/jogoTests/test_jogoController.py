import unittest
from unittest.mock import MagicMock, patch

from app.controllers.jogoController import JogoController


class TestJogoController(unittest.TestCase):
    def setUp(self):
        self.jogo_service = MagicMock()
        self.genero_service = MagicMock()
        self.controller = JogoController(self.jogo_service, self.genero_service)

    @patch("builtins.input", side_effect=["1"])
    def test_listar_jogos_opcao_1(self, mock_input):
        with patch("builtins.print") as mock_print:
            self.controller.menu()
            self.jogo_service.listar_jogos.assert_called_once()

    @patch("builtins.input", side_effect=["2", "God of War"])
    def test_buscar_jogo_opcao_2(self, mock_input):
        with patch("builtins.print"):
            self.controller.menu()
            self.jogo_service.buscar_jogo_por_nome.assert_called_once_with("God of War")

    @patch("builtins.input", side_effect=[
        "3",
        "God of War",
        "Ação e mitologia",
        "2022-10-20",
        "Ação, Aventura",
        "Santa Monica Studio",
        "199.99"
    ])
    def test_adicionar_jogo_opcao_3(self, mock_input):
        genero_mock = MagicMock()
        genero_mock.nome = "Ação"
        self.genero_service.buscar_ou_criar.side_effect = lambda nome: genero_mock

        with patch("builtins.print"):
            self.controller.menu()
            self.jogo_service.adicionar_jogo.assert_called_once()
            args = self.jogo_service.adicionar_jogo.call_args[0]
            self.assertEqual(args[0], "God of War")
            self.assertEqual(args[1], "Ação e mitologia")

    @patch("builtins.input", side_effect=[
        "4",
        "God of War",
        "God of War: Ragnarok",
        "Continuação",
        "2022-11-09",
        "Ação, Mitologia",
        "Santa Monica",
        "249.99"
    ])
    def test_editar_jogo_opcao_4(self, mock_input):
        genero_mock = MagicMock()
        self.genero_service.buscar_ou_criar.side_effect = lambda nome: genero_mock

        with patch("builtins.print"):
            self.controller.menu()
            self.jogo_service.atualizar_jogo.assert_called_once()

    @patch("builtins.input", side_effect=["5", "God of War"])
    def test_excluir_jogo_opcao_5(self, mock_input):
        with patch("builtins.print"):
            self.controller.menu()
            self.jogo_service.remover_jogo.assert_called_once_with("God of War")

    @patch("builtins.input", side_effect=["9"])
    def test_opcao_invalida(self, mock_input):
        with patch("builtins.print") as mock_print:
            self.controller.menu()
            mock_print.assert_any_call("Opção inválida.")


if __name__ == "__main__":
    unittest.main()
