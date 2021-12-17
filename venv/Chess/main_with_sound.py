#imported libraries

from engine_with_sound import TreeNode as t 
import pygame as pg
import engine_with_sound as Engine
from pygame.locals import *
import time

#global variables

#initilizing pyagme just in case 

pg.init()

# ---Window---

WIDTH = 750
HEIGHT = 900
MAX_FPS = 15


# ---Game---

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


    
# add a value to each piece in the dictionary: 
def addPieceValue(): 
    pass
    #here i am trying to add another value to each key which indicates the vallue fo each peice. 
    #this is crucial in terms of being able to map out the
    #weight of the edges later on with the recommendation system 

# loading images function 
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



def drawGS(screen,gs): 
    drawBoard(screen)
    drawPieces(screen,gs.BOARD, SQ_SIZE)
    
    

def drawBoard(screen):
    colors = [WHITE, GREEN]
    for row in range(MATRIX_DIM):
        for square in range(MATRIX_DIM):
            color = colors[((row+square)%2)]
            pg.draw.rect(screen, color, pg.Rect(square*SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            
def drawPieces(screen,BOARD, SQ_SIZE):
    for row in range(MATRIX_DIM):
        for square in range(MATRIX_DIM):
            piece = BOARD[row][square]
            if piece != "--":
                screen.blit(PIECES[piece][1], pg.Rect(square*SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))





def blitMove(screen,move): 
    text = move.strNotation()
    on = True
    while on == True: 
         text = font_obj.render(text, True,WHITE)
         textrect = text.get_rect()
         textrect.center = (500, 250)
         screen.blit(text,textrect)
    
    time.sleep(1)
    on = False




def castling(bool, move, root): 
    #obtain a boolean from a button
    castling_req = False
    if castling_req is True:
        king = move.BOARD[move.startRow][move.startCol]
        rook = move.BOARD[move.endRow][move.endCol]
        a  = root.search(king)
        b = root.search(rook)
        if a and b == None: 
            pass #do the castling 

def removeFromTree(root,node):
    move_text = node.getNotationFull()
    root.remove(root,move_text)

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
    wood_img = pg.transform.scale(pg.image.load("venv/Chess/images/wood.jpg"),(WIDTH, HEIGHT))
    screen.blit(wood_img, [0, 0])
    #button class 
    
            

    #drawing on the screen 
    load_images()
    root = t('e4')

    # debug 
    print(PIECES)

    # ---including engine---
    gs =  Engine.GameState()
    val = 1
    gs.soundval(val)
    drawGS(screen,gs)
    running = True 
    print(HEIGHT-HEIGHT//2.5)
    print(WIDTH//100)
    undoButton = Engine.button(WIDTH//100,HEIGHT-HEIGHT//2.5,'UNDO',screen)
    resetButton = Engine.button(WIDTH//100+170,HEIGHT-HEIGHT//2.5,'RESET',screen)
    quitButton = Engine.button(WIDTH//100+340,HEIGHT-HEIGHT//2.5,'QUIT',screen)
    castleButton = Engine.button(WIDTH//100,HEIGHT-HEIGHT//2.5 + 70, 'CASTLE-ME',screen)
    soundButtonOn = Engine.button(WIDTH//100+170,HEIGHT-HEIGHT//2.5+140,'ON',screen)
    soundButtonOff = Engine.button(WIDTH//100+340,HEIGHT-HEIGHT//2.5+140,'OFF',screen) 
    quitButton.draw_button()
    resetButton.draw_button()
    undoButton.draw_button()
    castleButton.draw_button()
    myfont = pg.font.SysFont("public-sans", 50)
    sound = myfont.render("SOUND", 1, (255,255,0))
    screen.blit(sound, (WIDTH//100+10,HEIGHT-HEIGHT//2.5+150))
    zombiestxt = myfont.render("ZOMBIES", 1, (255,255,0))
    screen.blit(zombiestxt, (WIDTH//100+530,HEIGHT-HEIGHT//1+10))
    soundOn = pg.image.load('venv/Chess/images/on.png')
    soundOff = pg.image.load('venv/Chess/images/off.png')
    soundOn = pg.transform.scale(soundOn, (325, 50))
    soundOff = pg.transform.scale(soundOff, (325, 50))
    screen.blit(soundOn, (WIDTH//100+170,HEIGHT-HEIGHT//2.5+140))


    klicked_SQ = ()
    klick_PL = []
    while running:
    
        for EVENT in pg.event.get(): 
            if EVENT.type == pg.QUIT: 
                running = False

            #key down
            # here i am just making sure that we handle mouse events (moving pieces etc) 

            elif EVENT.type == pg.MOUSEBUTTONDOWN: 

                #Button Operations
                posb = pg.mouse.get_pos()
                if WIDTH//100 <= posb[0] <= WIDTH//100 + 150 and HEIGHT-HEIGHT//2.5 <= posb[1] <= HEIGHT-HEIGHT//2.5 + 50:
                    gs.undoMove()
                    screen.blit(wood_img, [0, 0])
                    gs.drawZombies(screen,PIECES)
                    
                if WIDTH//100+170 <= posb[0] <= WIDTH//100 + 170 + 150 and HEIGHT-HEIGHT//2.5 <= posb[1] <=HEIGHT-HEIGHT//2.5 + 50:
                    gs.__init__()
                    root.__init__('e4')
                    screen.blit(wood_img, [0, 0])
                    continue
                if WIDTH//100+340 <= posb[0] <= WIDTH//100+ 340 + 155 and HEIGHT-HEIGHT//2.5 <= posb[1] <= HEIGHT-HEIGHT//2.5 + 50:
                    running = False

                if WIDTH//100 <= posb[0] <= WIDTH//100 + 150 and HEIGHT-HEIGHT//2.5 + 70 <= posb[1] <= HEIGHT-HEIGHT//2.5 + 70 + 50:
                    print('CASTLE-ME')

                if WIDTH//100+170 <= posb[0] <= WIDTH//100 + 170 + 150 and HEIGHT-HEIGHT//2.5 + 140 <= posb[1] <= HEIGHT-HEIGHT//2.5 + 140 + 50:
                    screen.blit(soundOn, (WIDTH//100+170,HEIGHT-HEIGHT//2.5+140))
                    val = 1            
                    gs.soundval(val)

                if WIDTH//100 + 340 <= posb[0] <= WIDTH-WIDTH//100 + 340 + 215 and HEIGHT-HEIGHT//2.5 + 140 <= posb[1] <= HEIGHT-HEIGHT//2.5 + 140 + 50:
                    screen.blit(soundOff, (WIDTH//100+170,HEIGHT-HEIGHT//2.5+140))             
                    val = 0
                    gs.soundval(val)

                #Translating pixel to row,col coord
                pos = pg.mouse.get_pos()
                col, row = pos[0]//SQ_SIZE , pos[1]//SQ_SIZE
                coordinateRowColumn = [row,col]  
                piece = gs.getPiece(coordinateRowColumn)



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
            quitButton.buttonColorManage(posbut,undoButton,resetButton,quitButton,castleButton)
            castleButton.buttonColorManage(posbut,undoButton,resetButton,quitButton,castleButton)
            screen.blit(sound, (WIDTH//100+10,HEIGHT-HEIGHT//2.5+150))
            if val == 0:
                screen.blit(soundOff, (WIDTH//100+170,HEIGHT-HEIGHT//2.5+140))
            elif val == 1:
                screen.blit(soundOn, (WIDTH//100+170,HEIGHT-HEIGHT//2.5+140))


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
