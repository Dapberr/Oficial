import pygame
import map

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load("assets/tiles/casa.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -20)

class Gym1(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load("assets/tiles/gym1.png")
        self.rect = self.image.get_rect(topleft = pos)


class Gym2(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load("assets/tiles/gym2.png")
        self.rect = self.image.get_rect(topleft = pos)


class Gym3(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load("assets/tiles/gym3.jpg")
        self.rect = self.image.get_rect(topleft = pos)

class Gym4(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load("assets/tiles/gym4.jpg")
        self.rect = self.image.get_rect(topleft = pos)

class Gym5(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load("assets/tiles/gym5.jpg")
        self.rect = self.image.get_rect(topleft = pos)

class Gym6(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load("assets/tiles/gym6.jpg")
        self.rect = self.image.get_rect(topleft = pos)

class Centro_Pokemon(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load("assets/tiles/centro pokemon.jpg")
        self.rect = self.image.get_rect(topleft = pos)

class Laboratorio(pygame.sprite.Sprite):
    def __init__(self,pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load("assets/tiles/laboratorio.jpg")
        self.rect = self.image.get_rect(topleft = pos)
