import pygame
import map
from Tiles_Pokemon import Tile, Gym1, Gym2, Gym3, Gym4, Gym5, Gym6, Centro_Pokemon, Laboratorio
from ash import Ash

class Nivel:
    def __init__(self):
        self.Screen = pygame.display.get_surface()
        self.Sprites_deFondo = pygame.sprite.Group()
        self.Obstaculos = pygame.sprite.Group()

        self.crearMapa()

    def crearMapa(self):
        for row_index, row in enumerate(map.mapa):
            for col_index, col in enumerate(row):
                x = col_index * 64
                y = row_index * 56
                if col == "X":
                    Tile((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "A":
                    Ash((x,y), [self.Sprites_deFondo], self.Obstaculos)
                if col == "1":
                    Gym1((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "2":
                    Gym2((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "3":
                    Gym3((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "4":
                    Gym4((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "5":
                    Gym5((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "6":
                    Gym6((x,y), [self.Sprites_deFondo, self.Obstaculos])
                if col == "L":
                    Laboratorio((x,y),[self.Sprites_deFondo, self.Obstaculos])
                if col == "C":
                    Centro_Pokemon((x,y),[self.Sprites_deFondo, self.Obstaculos])

    def corre(self):
        self.Sprites_deFondo.draw(self.Screen)
        self.Sprites_deFondo.update()