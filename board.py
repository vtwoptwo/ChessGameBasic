import pygame as pg
import sys

WIDTH = 660
HEIGHT = 490
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (142, 142, 142)
SILVER = (192, 192, 192)
GREEN = (0, 128, 0)
BROWN = (150, 75, 0)
screen = pg.display.set_mode((WIDTH, HEIGHT))

pg.init()
clock = pg.time.Clock()
icon = pg.image.load('chess_piece_king.png')
pg.display.set_caption('Chess')
pg.display.set_icon(icon)

color = {True: WHITE, False: BLACK}
current_color = True
target_square = None
turn = "white"

while True:
    screen.fill(GREY)
    pg.draw.rect(screen, BROWN, (20, 20, 440, 440))
    COLOUR = SILVER if turn == "white" else BLACK

    for row in range(8):
        for square in range(8):
            pg.draw.rect(screen, color[current_color], ((40 + (square * 50)), 40 + (row * 50), 50, 50))
            current_color = not current_color
        current_color = not current_color

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    pg.display.update()

