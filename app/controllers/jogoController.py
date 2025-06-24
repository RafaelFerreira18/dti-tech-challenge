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
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            self.jogo_service.listar_jogos()

        elif opcao == "2":
            nome_buscar = input("Nome do jogo a ser buscado: ")
            jogo = self.jogo_service.buscar_jogo_por_nome(nome_buscar)

        elif opcao == "3":
            nome = input("Nome do jogo: ")
            descricao = input("Descrição do jogo: ")
            ano_lancamento = input("Ano de lançamento do jogo (YYYY-MM-DD): ")
            generos_input = input("Gêneros do jogo (Separe por vírgula): ")
            empresa = input("Empresa desenvolvedora do jogo: ")
            preco = float(input("Preço do jogo: "))

            generos = [self.genero_service.buscar_ou_criar(g.strip()) for g in generos_input.split(",")]

            self.jogo_service.adicionar_jogo(
                nome, descricao, ano_lancamento, generos, empresa, preco
            )

        elif opcao == "4":
            nome_editar = input("Nome do jogo a ser editado: ")
            novo_nome = input("Novo nome do jogo: ")
            nova_descricao = input("Nova descrição do jogo: ")
            novo_ano = input("Novo ano de lançamento (YYYY-MM-DD): ")
            novos_generos = input("Novos gêneros (Separe por vírgula): ")
            nova_empresa = input("Nova empresa desenvolvedora: ")
            novo_preco = int(input("Novo preço: "))

            generos = [self.genero_service.buscar_ou_criar(g.strip()) for g in novos_generos.split(",")]

            self.jogo_service.atualizar_jogo(
                nome_editar, novo_nome, nova_descricao, novo_ano, generos, nova_empresa, novo_preco
            )

        elif opcao == "5":
            nome_excluir = input("Nome do jogo a ser excluído: ")
            self.jogo_service.remover_jogo(nome_excluir)

        elif opcao == "0":
            return

        else:
            print("Opção inválida. Tente novamente.")
