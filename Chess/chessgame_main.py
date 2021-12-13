#imported libraries

import pygame as pg

from Chess import chess_engine


import pygame as pg

#global variables


# ---Window---

WIDTH = 750
HEIGHT = 500
screen = pg.display.set_mode((WIDTH, HEIGHT))

# ---Game---

MATRIX_DIM = 8 
SQ_SIZE = 500 // MATRIX_DIM



# ---Colors---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
BROWN = (150, 75, 0)

# ---Images---



icon = pg.image.load('bK.png')
pg.init()
pg.display.set_caption('Chess')
pg.display.set_icon(icon)

color = {True: WHITE, False: BLACK}
current_color = True

while True:
    screen.fill(BLACK)
    pg.draw.rect(screen, BROWN, (20, 20, 440, 440))
    for row in range(8):
        for square in range(8):
            pg.draw.rect(screen, color[current_color], ((40 + (square * 50)), 40 + (row * 50), 50, 50))
            current_color = not current_color
        current_color = not current_color

    pg.display.update()