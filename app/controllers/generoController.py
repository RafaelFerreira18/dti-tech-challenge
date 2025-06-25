class GeneroController:
    def __init__(self, genero_service):
        self.genero_service = genero_service

    def menu(self):
        print("\n==== MENU DE GÊNEROS ====")
        print("1. Listar Gêneros")
        print("2. Buscar ou criar Gênero")
        print("3. Editar Gênero")
        print("4. Excluir Gênero")
        print("0. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ").strip()

        try:
            if opcao == "1":
                self.genero_service.listar_generos()

            elif opcao == "2":
                nome = input("Nome do gênero: ").strip()
                if not nome:
                    raise ValueError("Nome do gênero não pode ser vazio.")
                genero = self.genero_service.buscar_ou_criar(nome)
                print(f"Gênero encontrado ou criado: {genero.nome}")

            elif opcao == "3":
                nome_editar = input("Nome do gênero a ser editado: ").strip()
                novo_nome = input("Novo nome do gênero: ").strip()
                if not nome_editar or not novo_nome:
                    raise ValueError("Ambos os nomes devem ser informados.")
                self.genero_service.atualizar_genero(nome_editar, novo_nome)
                print(f"Gênero atualizado para: {novo_nome}")

            elif opcao == "4":
                nome_excluir = input("Nome do gênero a ser excluído: ").strip()
                if not nome_excluir:
                    raise ValueError("Nome do gênero não pode ser vazio.")
                self.genero_service.remover_genero(nome_excluir)
                print(f"Gênero '{nome_excluir}' removido com sucesso.")

            elif opcao == "0":
                return

            else:
                print("Opção inválida. Tente novamente.")

        except ValueError as ve:
            print(f"Erro de entrada: {ve}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")