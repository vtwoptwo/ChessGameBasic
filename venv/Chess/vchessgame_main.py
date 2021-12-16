#imported libraries

from vchessgame_engine import TreeNode as t 
import pygame as pg
import vchessgame_engine as Engine
from pygame.locals import *
import time

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



def drawZombies(screen,BOARD):
    for row in range(MATRIX_DIM):
        for square in range(MATRIX_DIM):
            piece = BOARD[row][square]
            if piece != "--":
<<<<<<< HEAD
                if piece[0] == 'w':
                    screen.blit(PIECES[piece], pg.Rect(500, row * ZSQ_SIZE, ZSQ_SIZE, ZSQ_SIZE))
                else:
                    screen.blit(PIECES[piece], pg.Rect(540, row * ZSQ_SIZE, ZSQ_SIZE, ZSQ_SIZE))
=======
                screen.blit(PIECES[piece][1], pg.Rect(square*ZSQ_SIZE, row * ZSQ_SIZE, ZSQ_SIZE, ZSQ_SIZE))
>>>>>>> 822c9fcfd81acf55bcec5b2f387f4b337a049102


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


def movesMadeTree(root, move):
    move_text = move.getNotationFull()
    Engine.insert(root, move_text)
    Engine.print_tree(root)

def castling(bool, move, root): 
    #obtain a boolean from a button
    castling_req = False
    if castling_req is True:
        king = move.BOARD[move.startRow][move.startCol]
        rook = move.BOARD[move.endRow][move.endCol]
        a  = root.search(king)
        b = root.search(rook)
        if a and b == None: 
            pass #do the castling with whatever


#button class 

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


    #button class 
    class button():
        
        #colours for button and text
        
        
        button_col = (255, 255, 255)
        hover_col = (75, 225, 255)
        click_col = (50, 150, 255)
        text_col = (0,0,0)
        width = 80
        height = 50
        

        def __init__(self, x, y, text):
            self.x = x
            self.y = y
            self.text = text

        def draw_button(self):

            global clicked
            action = False
            clicked = False
            font = pg.font.SysFont('Constantia', 20)
            #get mouse position
            #pos = pg.mouse.get_pos()

            #create pygame Rect object for the button
            button_rect = Rect(self.x, self.y, self.width, self.height)
            
            #check mouseover and clicked conditions
            
            pg.draw.rect(screen, self.button_col, button_rect)
            
            #add shading to button
            pg.draw.line(screen, BLACK, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
            pg.draw.line(screen, BLACK, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

            #add text to button
            text_img = font.render(self.text, True, self.text_col)
            text_len = text_img.get_width()
            screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 18))
            return action


    def buttonColorManage(pos):
            if WIDTH-WIDTH//3 <= pos[0] <= WIDTH-WIDTH//3 + 80 and HEIGHT//100 <= pos[1] <= HEIGHT//100 + 50:
                undoButton.button_col = (GREEN)
                resetButton.button_col = (WHITE)
                resetButton.draw_button()
                quitButton.button_col = (WHITE)
                quitButton.draw_button()
                undoButton.draw_button()
            elif WIDTH-WIDTH//3+85 <= pos[0] <= WIDTH-WIDTH//3 + 165 and HEIGHT//100 <= pos[1] <= HEIGHT//100 + 50:
                resetButton.button_col = (GREEN)
                undoButton.button_col = (WHITE)
                undoButton.draw_button()
                quitButton.button_col = (WHITE)
                quitButton.draw_button()
                resetButton.draw_button()
            elif WIDTH-WIDTH//3+170 <= pos[0] <= WIDTH-WIDTH//3 + 250 and HEIGHT//100 <= pos[1] <= HEIGHT//100 + 50:
                quitButton.button_col = (GREEN)
                undoButton.button_col = (WHITE)
                undoButton.draw_button()
                resetButton.button_col = (WHITE)
                resetButton.draw_button()
                quitButton.draw_button()
            else:
                undoButton.button_col = (WHITE)
                undoButton.draw_button()
                resetButton.button_col = (WHITE)
                resetButton.draw_button()
                quitButton.button_col = (WHITE)
                quitButton.draw_button()
            

    #drawing on the screen 
    load_images()
    root = Engine.TreeNode("e4")

    # debug 
    print(PIECES)

    # ---including engine---
    gs =  Engine.GameState()
    screen.fill(BROWN)
    
    drawGS(screen,gs)
    running = True 
    print(HEIGHT//100)
    print(WIDTH-WIDTH//3)
    undoButton = button(WIDTH-WIDTH//3,HEIGHT//100,'UNDO')
    resetButton = button(WIDTH-WIDTH//3+85,HEIGHT//100,'RESET')
    quitButton = button(WIDTH-WIDTH//3+170,HEIGHT//100,'QUIT')
    quitButton.draw_button()
    resetButton.draw_button()
    undoButton.draw_button()

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
                if WIDTH-WIDTH//3 <= posb[0] <= WIDTH-WIDTH//3 + 100 and HEIGHT//100 <= posb[1] <= HEIGHT//100 + 50:
                    gs.undoMove()
                if WIDTH-WIDTH//3+85 <= posb[0] <= WIDTH-WIDTH//3 + 165 and HEIGHT//100 <= posb[1] <= HEIGHT//100 + 50:
                    gs.__init__()
                    continue
                if WIDTH-WIDTH//3+170 <= posb[0] <= WIDTH-WIDTH//3 + 250 and HEIGHT//100 <= posb[1] <= HEIGHT//100 + 50:
                    running = False


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
                    movesMadeTree(root, move)
                    gs.makeMove(move)
                    
                    if len(gs.Zombies) != 0:
                      for zombie in gs.Zombie: 
                          for i in range(7): 
                              for j in range(8):
                                screen.blit

                    # if z in zombies.


                    klicked_SQ = () 
                    klick_PL = []

            posbut = pg.mouse.get_pos()
            buttonColorManage(posbut)
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