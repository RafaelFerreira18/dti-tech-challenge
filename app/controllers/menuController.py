class MenuController:
    def __init__(self, jogo_controller, genero_controller):
        self.jogo_controller = jogo_controller
        self.genero_controller = genero_controller

    def menu(self):
        while True:
            print("\n==== MENU PRINCIPAL ====")
            print("1. Gerenciar Jogos")
            print("2. Gerenciar Gêneros")
            print("0. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.jogo_controller.menu()
            elif opcao == "2":
                self.genero_controller.menu()
            elif opcao == "0":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")