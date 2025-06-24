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
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            self.genero_service.listar_generos()

        elif opcao == "2":
            nome = input("Nome do gênero: ")
            genero = self.genero_service.buscar_ou_criar(nome)

        elif opcao == "3":
            nome_editar = input("Nome do gênero a ser editado: ")
            novo_nome = input("Novo nome do gênero: ")
            self.genero_service.atualizar_genero(nome_editar, novo_nome)

        elif opcao == "4":
            nome_excluir = input("Nome do gênero a ser excluído: ")
            self.genero_service.remover_genero(nome_excluir)

        elif opcao == "0":
            return

        else:
            print("Opção inválida. Tente novamente.")
