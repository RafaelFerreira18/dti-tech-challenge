<<<<<<< dev
from app.config.database import db
from app.controllers import GeneroController, JogoController, MenuController
from app.repositories import GeneroRepository, JogoRepository
from app.services import GeneroService, JogoService
=======
from app.controllers.generoController import GeneroController
from app.controllers.jogoController import JogoController
from app.controllers.menuController import MenuController
>>>>>>> main


def initialize_database():
    db.connect()

def close_database():
    db.close()

def main():
    genero_repository = GeneroRepository()
    genero_service = GeneroService(genero_repository)
    genero_ctrl = GeneroController(genero_service)
    
    jogo_repository = JogoRepository()
    jogo_service = JogoService(jogo_repository)
    jogo_ctrl = JogoController(jogo_service, genero_service)

    menu = MenuController(jogo_ctrl, genero_ctrl)
    menu.menu()

if __name__ == "__main__":
    initialize_database()
    main()
    close_database()
