#imported libraries

from zanechessgame_engine import TreeNode as t 
import pygame as pg
import zanechessgame_engine as Engine
from pygame.locals import *
import time

#global variables

#initilizing pyagme just in case 

pg.init()

# ---Window---
# Dimensions and FPS for our game
WIDTH = 750
HEIGHT = 900
MAX_FPS = 15


# ---Game---
# Game Specifics: Matrix_Dim is our divisor for dividing our board into and 8x8
# SQ_SIZE indicates the size of the squares
MATRIX_DIM = 8 
SQ_SIZE = 500 // MATRIX_DIM

ZSQ_SIZE = 240 // MATRIX_DIM 

# ---Colors---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 102, 0)
BROWN = (51, 0, 102)

# ---Images---
font_obj = pg.font.Font('freesansbold.ttf', 32)

# ---Images---

PIECES= {} 
#implementation of a dictionary high space complexity low time complexity 
#static

# loading images function
# This function fills the PIECES dictionary with a piece string and its associated image in a str:image format for each piece respectively
def load_images(): 
    pieces = ["bR", "bN", "bB", "bQ", "bK", "wB", "wN", "wR","wQ", "wK", "bP", "bP", "wP" ]
    for piece in pieces: 
        imagepiece = pg.transform.scale(pg.image.load( "venv/Chess/images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
        if piece[1] == "P":
            case = {piece: (6,imagepiece)}
        if piece[1] == "B":
            case = {piece: (5,imagepiece)}
        if piece[1] == "N":
            case = {piece: (4,imagepiece)}
        if piece[1] == "R":
            case = {piece: (3,imagepiece)}
        if piece[1] == "Q":
            case = {piece: (2,imagepiece)}
        if piece[1] == "K":
            case = {piece: (1,imagepiece)}
        PIECES.update(case)
    print(PIECES)

#include hashtable 

#drawGS draws our gamestate and keeps up with the changes of our matrix in the engine
def drawGS(screen,gs): 
    drawBoard(screen)
    drawPieces(screen,gs.BOARD, SQ_SIZE)

    
# Specifically handles board graphics and is a child function of drawGS
def drawBoard(screen):
    colors = [WHITE, GREEN]
    for row in range(MATRIX_DIM):
        for square in range(MATRIX_DIM):
            color = colors[((row+square)%2)]
            pg.draw.rect(screen, color, pg.Rect(square*SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            
# Specifically handles Piece graphics and is a child function of drawGS        
def drawPieces(screen,BOARD, SQ_SIZE):
    for row in range(MATRIX_DIM):
        for square in range(MATRIX_DIM):
            piece = BOARD[row][square]
            if piece != "--":
                screen.blit(PIECES[piece][1], pg.Rect(square*SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
        

#main driver code

def main():
    

    # --- setup ---
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.init()
    icon = pg.image.load( "venv/Chess/images/bQ.png")
    pg.display.set_caption('Chess')
    pg.display.set_icon(icon)   
    clock = pg.time.Clock() # important for restricting fram rate
    wood_img = pg.transform.scale(pg.image.load("venv/Chess/images/wood.jpg"),(WIDTH, HEIGHT)) #background image load
    screen.blit(wood_img, [0, 0])
    
            

    #drawing on the screen 
    load_images()

    #Initializes our binary search tree with a root of position e4
    root = t('e4')

    # ---including engine---
    gs =  Engine.GameState()
    
    drawGS(screen,gs) # Calling drawGS
    running = True #our main game loop boolean and is used to quit upon the click of the quit button

    #Initializing Buttons
    undoButton = Engine.button(WIDTH//100,HEIGHT-HEIGHT//2.5,'UNDO',screen)
    resetButton = Engine.button(WIDTH//100+170,HEIGHT-HEIGHT//2.5,'RESET',screen)
    quitButton = Engine.button(WIDTH//100+340,HEIGHT-HEIGHT//2.5,'QUIT',screen)
    castleButton = Engine.button(WIDTH//100,HEIGHT-HEIGHT//2.5 + 70, 'CASTLE-ME',screen)
    #Displaying the Buttons
    quitButton.draw_button()
    resetButton.draw_button()
    undoButton.draw_button()
    castleButton.draw_button()

    #Klicked_SQ will hold the pixel x,y of our mouse upon click
    klicked_SQ = ()
    #Klicked_PL is a list of Klicked_SQ will help us manage peice movement
    klick_PL = []

    #game loop
    while running:
        
        # Allows us to quit when pygame receives a quit event
        for EVENT in pg.event.get(): 
            if EVENT.type == pg.QUIT: 
                running = False

            #checks if event type is a mouse click if yes the code below will run
            elif EVENT.type == pg.MOUSEBUTTONDOWN: 

                #Button Operations
                #this posb gets the current position of our mouse upon click 
                posb = pg.mouse.get_pos()

                # the next 4 if statements are intervals of pixels that tell us which button we are missing
                if WIDTH//100 <= posb[0] <= WIDTH//100 + 150 and HEIGHT-HEIGHT//2.5 <= posb[1] <= HEIGHT-HEIGHT//2.5 + 50:
                    gs.undoMove(root)
                    screen.blit(wood_img, [0, 0])
                    gs.drawZombies(screen,PIECES)
                    continue
                if WIDTH//100+170 <= posb[0] <= WIDTH//100 + 170 + 150 and HEIGHT-HEIGHT//2.5 <= posb[1] <=HEIGHT-HEIGHT//2.5 + 50:
                    gs.__init__()
                    root.__init__("e4")
                    screen.blit(wood_img, [0, 0])
                    continue
                if WIDTH//100+340 <= posb[0] <= WIDTH//100+ 340 + 215 and HEIGHT-HEIGHT//2.5 <= posb[1] <= HEIGHT-HEIGHT//2.5 + 50:
                    running = False

                if WIDTH//100 <= posb[0] <= WIDTH//100 + 150 and HEIGHT-HEIGHT//2.5 + 70 <= posb[1] <= HEIGHT-HEIGHT//2.5 + 70 + 50:
                    print('CASTLE-ME')
                    if gs.whiteMove:
                        if root.rcsearch(root,'e1') is None and root.rcsearch(root,'h1') is None and root.rcsearch(root,'f1') is not None and root.rcsearch(root,'g1') is not None:
                            Wking = Engine.Move((7,4), (7,6), gs.BOARD)
                            gs.makeMove(Wking)
                            Wrook = Engine.Move((7,7),(7,5), gs.BOARD)
                            gs.makeMove(Wrook)
                        else:
                            print("Castle Not Allowed For White")
                    else:
                        if root.rcsearch(root,'d8') is None and root.rcsearch(root,'a8') is None and root.rcsearch(root,'b8') is not None and root.rcsearch(root,'c8') is not None:
                            Bking = Engine.Move((0,3), (0,1), gs.BOARD)
                            gs.makeMove(Bking)
                            Brook = Engine.Move((0,0),(0,2),gs.BOARD)
                            gs.makeMove(Brook)
                        else:
                            print("Castle Not Allowed For Black")




                #Translating pixel to row,col coord
                pos = pg.mouse.get_pos()
                col, row = pos[0]//SQ_SIZE , pos[1]//SQ_SIZE
                coordinateRowColumn = [row,col]  
                piece = gs.getPiece(coordinateRowColumn)


                print(piece)

                # base case invalid move, if invalid resets klick lists
                if klicked_SQ == (row,col) or row >= 8 or col >= 8: # checks if click is outside of chess board if true
                    klicked_SQ = ()                                 # clears clicked values
                    klick_PL = []
                
                else:

                    klicked_SQ = (row, col)
                    klick_PL.append(klicked_SQ)
                    print(klick_PL)

                # while len(klick_PL)==1: 
                #     #identify the move clicked create a potential move pMove()
                #     if EVENT.type == pg.KEYDOWN: 
                #         if EVENT.key == pg.K_e: #e for escape 
                #             klicked_SQ = ()
                #             klick_PL = []
                #             print(klick_PL)

                #     #add the show recommendation
                #     # print(move.getGraph())


                if len(klick_PL) == 2:
                    move = Engine.Move(klick_PL[0], klick_PL[1], gs.BOARD)
                    
                    print(move.getNotationStart())
                    # blitMove(screen,move)
                    root.movesMadeTree(root, move)
                    
                    gs.makeMove(move)
                    
                    if len(gs.Zombies) != 0:
                        gs.drawZombies(screen, PIECES)
                    

                    # if z in zombies.


                    klicked_SQ = () 
                    klick_PL = []

            posbut = pg.mouse.get_pos()
            undoButton.buttonColorManage(posbut,undoButton,resetButton,quitButton,castleButton)
            resetButton.buttonColorManage(posbut,undoButton,resetButton,quitButton,castleButton)
            quitButton.buttonColorManage(posbut,undoButton,resetButton,quitButton,castleButton)
            castleButton.buttonColorManage(posbut,undoButton,resetButton,quitButton,castleButton)
            #elif EVENT.type == pg.KEYDOWN:
                #if EVENT.key ==  pg.K_u: #u for undo
                    #gs.undoMove()    


        drawGS(screen, gs)
        clock.tick(MAX_FPS)
        pg.display.flip()
        
        pg.display.update()



#within the driver code we have functions which help us manage the graphics of the game 


                




# if __name__ == "__main__": 

main()