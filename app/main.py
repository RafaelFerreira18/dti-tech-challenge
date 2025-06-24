from app.controllers.generoController import GeneroController
from app.controllers.jogoController import JogoController
from app.controllers.menuController import MenuController


def main():
    jogo_ctrl = JogoController()
    genero_ctrl = GeneroController()
    menu = MenuController(jogo_ctrl, genero_ctrl)
    menu.menu()

if __name__ == "__main__":
    main()
