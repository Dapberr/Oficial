import sys
import pygame
from Niveles_pokemon import Nivel


class Pokemon:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1210, 670))
        pygame.display.set_caption("Pokemon Blinder")
        self.nivel = Nivel()


    def corre_juego(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill("grey")
            self.nivel.corre()
            pygame.display.update()


if __name__ == "__main__":
    main = Pokemon()
    main.corre_juego()
