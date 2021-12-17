#imported libraries

from types import ClassMethodDescriptorType
from typing import ByteString
from Chess.vchessgame_engine import TreeNode
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
PIECESNUM ={12: 'bP', 11: 'wP', 10: 'bB', 9: 'wB', 8: 'bN', 7: 'wN', 6: 'bR', 5: 'wR', 4: 'bQ', 3: 'wQ', 2: 'bK', 1: 'wK'}
#implementation of a dictionary high space complexity low time complexity 
#static


    
# add a value to each piece in the dictionary: 

    #here i am trying to add another value to each key which indicates the vallue fo each peice. 
    #this is crucial in terms of being able to map out the
    #weight of the edges later on with the recommendation system 

# loading images function 
def load_images(): 
    pieces = ["bR", "bN", "bB", "bQ", "bK", "wB", "wN", "wR","wQ", "wK", "bP", "bP", "wP" ]
    for piece in pieces: 
        imagepiece = pg.transform.scale(pg.image.load( "venv/Chess/images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
        if piece == "bP":
            case = {piece: (12,imagepiece)}
        if piece == "bB":
            case = {piece: (10,imagepiece)}
        if piece == "bN":
            case = {piece: (8,imagepiece)}
        if piece == "bR":
            case = {piece: (6,imagepiece)}
        if piece == "bQ":
            case = {piece: (4,imagepiece)}
        if piece == "bK":
            case = {piece: (2,imagepiece)}
        if piece == "wP":
            case = {piece: (11,imagepiece)}
        if piece == "wB":
            case = {piece: (9,imagepiece)}
        if piece == "wN":
            case = {piece: (7,imagepiece)}
        if piece == "wR":
            case = {piece: (5,imagepiece)}
        if piece == "wQ":
            case = {piece: (3,imagepiece)}
        if piece == "wK":
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
    createPIECESNUM()
    print("PIECESNUM:", PIECESNUM)

    #drawing on the screen 
    load_images()
    root = t('e4')

    # debug 
    print(PIECES)

    # ---including engine---
    gs =  Engine.GameState()
    
    drawGS(screen,gs)
    running = True 
    print(HEIGHT-HEIGHT//2.5)
    print(WIDTH//100)
    undoButton = Engine.button(WIDTH//100,HEIGHT-HEIGHT//2.5,'UNDO',screen)
    resetButton = Engine.button(WIDTH//100+170,HEIGHT-HEIGHT//2.5,'RESET',screen)
    quitButton = Engine.button(WIDTH//100+340,HEIGHT-HEIGHT//2.5,'QUIT',screen)
    castleButton = Engine.button(WIDTH//100,HEIGHT-HEIGHT//2.5 + 70, 'CASTLE-ME',screen)
    quitButton.draw_button()
    resetButton.draw_button()
    undoButton.draw_button()
    castleButton.draw_button()

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
                        sortZombies(gs)
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





main()




# TIME COMPLEXITIES

# Data Structures: 

# DS A: MATRIX
# for the matrix we actually change positions of pieces by having a time complexity of o(1)
# we take the x and y value separate for each predefined quare in the matrix and and can thus manipulate 
# piece movements in O(1) time

# # DS B:  BINARY SEARCH TREE

# The binary search tree time complexity to search for the pieces moved is O(logn)

# this is quite a complex process since when we undid move we also had to remove nodes form the tree account for three different Clases
#the node having children, the node having no children, the node had 1 child
# # this datas structure was created to check if a king or rook has been moved or not in order to 
# # implement a "castling functionality"

# we managed to tdo this with one of the kings 

# due to tiume constraints we were unable to do it for both sides of each color, but the king for each color castles with the rook closest to him 

# DS C: DICTIONARY

# we used dictionaries in several instances, mostly to create 
# conversions between piece location, piece notation, piece names and piece values 

# this could have easily been avoided by implementing a hash table form the beginning and individual piece
# classes, but this was realized too late and we could not implement it in time without changing everything 

# DS D: HEAP
# the heap was created in order to apply a bubble sorting algorithm 
# we ran into a few bugs once implemeing the heap but we think that with more time this would have been a problem which was easy to solve 

# in fact we recognize that we should have used a hash function to identify the pieces, 

# to be honest we had already created the hash function and were doing this 
# but later decided against it

# below you can see our implementation of the hash function 


# PIECES = {'bR': (3, "<Surface(62x62x32 SW)>"), 'bN': (4, "<Surface(62x62x32 SW)>"), 'bB': (5, "<Surface(62x62x32 SW)>"), 'bQ': (2, "<Surface(62x62x32 SW)>"), 'bK': (1, "<Surface(62x62x32 SW)>"), 'wB': (5, "<Surface(62x62x32 SW)>"), 'wN': (4, "<Surface(62x62x32 SW)>"), 'wR': (3, "<Surface(62x62x32 SW)>"), 'wQ': (2, "<Surface(62x62x32 SW)>"), 'wK': (1, "<Surface(62x62x32 SW)>"), 'bP': (6, "<Surface(62x62x32 SW)>"), 'wP': (6, "<Surface(62x62x32 SW)>")}
# HASHPIECESW = []
# HASHPIECESB = []


# def str_to_number(string):
#   number = 0
#   # A string in python is just a list of characters, with extra functions built around. So we can iterate over it using the index of each character.
#   # We will use then the index of each character to compose the exponent to which we have to raise the base, 128, for each of them.
#   for i in range(len(string)): 
#     exponent = len(string) - 1 - i # Exponents start at len(string) - 1, and decrease one by one upt to 0.
#     asc = ord(string[i]) # Compute the ascii number corresponding to that character at position i.
#     number += asc * (128**exponent) # Calculate the base-128 for this character at position i, and accumulate it in number
#   return number


# for piece in PIECES:
#     if piece[0] == 'w':
#         case = (piece + str(PIECES[piece][0]))
#         hase = str_to_number(case)
#         HASHPIECESW.append(hase)
#     if piece[0] == 'b':
#         case = (piece + str(PIECES[piece][0]))
#         hase = str_to_number(case)
#         HASHPIECESB.append(hase)


# print(HASHPIECESB)
# print(HASHPIECESW)


# ALGORITHMS: 

# binary search through a BST :) 

# sorting function for the heap :) 


# Attempted applications of quicksort which has a to,e complexity of 
# O(nlogn)

# def createPIECESNUM():
#     for piece in PIECES:
#         case = {PIECES[piece][0]: piece}
#         PIECESNUM.update(case)
#     return PIECESNUM

# def create_array(gs):
#     numZ = []
#     for i in gs.Zombies:
#         num = PIECES[i][0]
#         print("Number:", num)
#         numZ.append(num)
#     return numZ

# def undoArray(numZ): 
#     strZ =[]
#     for num in numZ:
#         string = PIECESNUM[num]
#         strZ.append(string)
#     return strZ

# def quicksort(gs): 
#     array = create_array(gs)
#     # sort function
#     if len(array) < 2:
#         return array # One or none elements, the subarray is already sorted
#     pivot = int(len(array) / 2) # Pick the element at the middle of the array as pivot
#     pivot_value = array[pivot]
#     left = [x for x in array[0:pivot] + array[pivot+1:] if x <= pivot_value] # The left sub array with all elements smaller or equal than pivot_value
#     right = [x for x in array[0:pivot] + array[pivot+1:] if x > pivot_value] # The right subarray with all the elements larger than pivot_value
#     return quicksort(left) + [pivot_value] + quicksort(right)
    
# def sortZombies(gs): 
#     gs.Zombies = undoArray(quicksort(gs))
#     return gs.Zombies



#Heap 

# the reason we use heap is because the heap is ideal for
#  constant updating situations such as when a piece dies and needs 
# to appear on the screen
# 
# furthermore the heap has a time complexity average case of O(1)
#  and worst case time complexity of O(1) 