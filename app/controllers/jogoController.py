from datetime import datetime


class JogoController:
    def __init__(self, jogo_service, genero_service):
        self.jogo_service = jogo_service
        self.genero_service = genero_service

    def menu(self):
        print("\n==== MENU DE JOGOS ====")
        print("1. Listar Jogos")
        print("2. Buscar Jogo por nome")
        print("3. Adicionar Jogo")
        print("4. Editar Jogo")
        print("5. Excluir Jogo")
        print("0. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ").strip()

        try:
            if opcao == "1":
                self.jogo_service.listar_jogos()

            elif opcao == "2":
                nome = input("Nome do jogo a ser buscado: ").strip()
                if not nome:
                    raise ValueError("Nome do jogo não pode ser vazio.")
                self.jogo_service.buscar_jogo_por_nome(nome)

            elif opcao == "3":
                nome = input("Nome do jogo: ").strip()
                if not nome:
                    raise ValueError("Nome não pode ser vazio.")

                descricao = input("Descrição do jogo: ").strip()

                data = input("Data de lançamento (YYYY-MM-DD): ").strip()
                try:
                    datetime.strptime(data, "%Y-%m-%d")
                except ValueError:
                    raise ValueError("Formato de data inválido.")

                generos_input = input("Gêneros (separados por vírgula): ").strip()
                if not generos_input:
                    raise ValueError("Informe pelo menos um gênero.")
                generos = [self.genero_service.buscar_ou_criar(g.strip()) for g in generos_input.split(",")]

                empresa = input("Empresa desenvolvedora: ").strip()
                if not empresa:
                    raise ValueError("Empresa não pode ser vazia.")

                try:
                    preco = float(input("Preço do jogo: ").strip())
                except ValueError:
                    raise ValueError("Preço inválido. Use ponto (.) para decimais.")

                self.jogo_service.adicionar_jogo(nome, descricao, data, generos, empresa, preco)

            elif opcao == "4":
                nome_antigo = input("Nome do jogo a ser editado: ").strip()
                novo_nome = input("Novo nome: ").strip()
                nova_descricao = input("Nova descrição: ").strip()
                nova_data = input("Nova data (YYYY-MM-DD): ").strip()
                datetime.strptime(nova_data, "%Y-%m-%d")
                generos_input = input("Novos gêneros (separados por vírgula): ").strip()
                generos = [self.genero_service.buscar_ou_criar(g.strip()) for g in generos_input.split(",")]
                nova_empresa = input("Nova empresa: ").strip()
                novo_preco = float(input("Novo preço: ").strip())

                self.jogo_service.atualizar_jogo(nome_antigo, novo_nome, nova_descricao, nova_data, generos, nova_empresa, novo_preco)

            elif opcao == "5":
                nome = input("Nome do jogo a ser excluído: ").strip()
                self.jogo_service.remover_jogo(nome)

            elif opcao == "0":
                return

            else:
                print("Opção inválida.")

        except ValueError as ve:
            print(f"Erro: {ve}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")