#imported libraries

import pygame as pg
import chessgame_engine as Engine


#global variables

#initilizing pyagme just in case 

pg.init()

# ---Window---

WIDTH = 750
HEIGHT = 500
MAX_FPS = 15


# ---Game---

MATRIX_DIM = 8 
SQ_SIZE = 500 // MATRIX_DIM


# ---Colors---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
BROWN = (150, 75, 0)

# ---Images---

PIECE_IMAGES= {} 
#implementation of a dictionary high space complexity low time complexity 
#static

# loading images function 
def load_images(): 
    pieces = ["bR", "bN", "bB", "bQ", "bK", "wB", "wN", "wR","wQ", "wK", "bP", "bP", "wP" ]
    for piece in pieces: 
        imagepiece = pg.transform.scale(pg.image.load( "venv/Chess/images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
        case = {piece:  imagepiece}
        PIECE_IMAGES.update(case)


def drawGS(screen,gs): 
    drawBoard(screen)
    drawPieces(screen,gs.BOARD)

def drawBoard(screen):
    colors = [WHITE, GREEN]
    for row in range(MATRIX_DIM):
        for square in range(MATRIX_DIM):
            color = colors[((row+square)%2)]
            pg.draw.rect(screen, color, pg.Rect(square*SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            
def drawPieces(screen,BOARD):
    for row in range(MATRIX_DIM):
        for square in range(MATRIX_DIM):
            piece = BOARD[row][square]
            if piece != "--":
                print(piece)
                screen.blit(PIECE_IMAGES[piece], pg.Rect(square*SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawGS(screen,gs): 
    drawBoard(screen)
    drawPieces(screen,gs.BOARD)


# --- piece class ---

#main driver code

def main():
    
   
    # --- setup ---
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.init()
    icon = pg.image.load( "venv/Chess/images/bQ.png")
    pg.display.set_caption('Chess')
    pg.display.set_icon(icon)   
    clock = pg.time.Clock()

    #exectuted once 
    load_images()    

    # debug 
    print(PIECE_IMAGES)

    # ---including engine---
    gs =  Engine.GameState()
    drawGS(screen,gs)
    running = True 
    
    klicked_SQ = ()
    klick_PL = []
    while running:
    
        for EVENT in pg.event.get(): 
            if EVENT.type == pg.QUIT: 
                running = False

            # here i am just making sure that we handle mouse events (moving pieces etc) 

            elif EVENT.type == pg.MOUSEBUTTONDOWN: 

                pos = pg.mouse.get_pos()
                col, row = pos[0]//SQ_SIZE , pos[1]//SQ_SIZE 
                 # base case invalid move 
                if klicked_SQ == (row,col): 
                    klicked_SQ = ()
                    klick_PL = []
                else: 
                    klicked_SQ = (row, col)
                    klick_PL.append(klicked_SQ)
                if len(klick_PL) == 2:
                    move = Engine.Move(klick_PL[0], klick_PL[1], gs.BOARD)
                    print(move.getNotation())
                    gs.makeMove(move)
                    klicked_SQ = () 
                    klick_PL = []

        drawGS(screen, gs)
        clock.tick(MAX_FPS)
        pg.display.flip()
        
        
        pg.display.update()



#within the driver code we have functions which help us manage the graphics of the game 


                




# if __name__ == "__main__": 

main()