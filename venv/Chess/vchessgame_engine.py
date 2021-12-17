import pygame as pg
from pygame.locals import *
class WGraph:
  def __init__(self):
    self.vertices = {}

  def add_vertex(self, value):
    if not value in self.vertices:
      self.vertices[value] = []
    return self.vertices[value]
  
  def add_edge(self, a, b, w): 
    if not a in self.vertices:
      return
    a_edges = self.vertices[a]
    if not b in a_edges:
      a_edges.append((b, w)) # Add a tuple of two elements, bearing the target vertex and the weight of the edge.
  
  def print(self):
    for vertex, edges in self.vertices.items():
      print(f'{vertex} -> {edges}')




class Zombies(): 
    def __init__(self): 
        self.whiteZombies = [
            ["wP""wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]

        self.blackZombies = [
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
        ]


class GameState():
    def __init__(self):
        # so far a 2d matrix 
        
        self.BOARD = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]

        self.whiteMove = True

        self.movehistory = [] # implementation of a stack :) this can be used to undo a move 
                                #if we undo a move there actually needs to be an implementation of some 
                                #rules...movehistory, versus backtracking? does it count as a move? 
        self.Zombies = []
    def drawZombies(self, screen, dict):
      wp = 0
      bp = 0 
      for zombie in self.Zombies: 
          if zombie[0] == "w": 
              screen.blit(dict[zombie][1],(500, 100+wp))
              wp += 45
          if zombie[0] == "b":
              screen.blit(dict[zombie][1],(600, 100+bp))
              bp += 45
          

    def getPiece(self,pos):
        if pos[0] >= 8 or pos[1] >= 8:
            return
        else:
            print(pos)
            return self.BOARD[pos[0]][pos[1]]
    
    # this function exectutes basic moves 
    # there are several exception cases which we will address with separate functions

    def makeMove(self, move): 
        if self.BOARD[move.endRow][move.endCol] != '--':
            self.Zombies.append(self.BOARD[move.endRow][move.endCol])
            print("Captured Pieces:",self.Zombies)
        if self.BOARD[move.startRow][move.startCol]  == "--": #check to make sure an empty square cant remove a peice
            return # if true program continues without making changes
        self.BOARD[move.startRow][move.startCol]  = "--"
        self.BOARD[move.endRow][move.endCol] = move.PieceMoved
        self.movehistory.append(move) # for an undo move, just pop 
        self.whiteMove = not self.whiteMove

        

    #including an undo function

    def undoMove(self):
        if len(self.movehistory) == 0:
            return # makes sure program doesnt crash if undo button is pressed and move history is empty
        else:
            if len(self.Zombies) != 0:
              self.Zombies.pop()
            umove = self.movehistory.pop()
            self.BOARD[umove.startRow][umove.startCol] = umove.PieceMoved
            self.BOARD[umove.endRow][umove.endCol] = umove.PieceDed
            self.whiteMove = not self.whiteMove
            

    def ValidMoves(): 
        pass


    #creating recommendation system using adjacency list and graphs
    
    def getGraph(self, move, library):
        piece = self.BOARD[move.startRow][move.StartCol]
        if piece == "bN":                                                                  
            pass
            #for all node in all possible nodes that the knight can reach in one node
            #tempgraphforknight.add_vertex(node)
            #for node in all possiblenodes()
            # w = weight of each destination node extracted from the dictionary
            #tempgraphadd_edge(piece_node, node, w) 
            # 
            # 

            #calculate shortest path node
            #

        if piece == "bK":
            pass
            #same implementation as above except generate a different legal moves function for different pieces
    



class pMove(): 
     # switching to true row and column notation with dictionaries 

    num_2_row = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    row_2_num = {v: k for k, v in num_2_row.items()}
    lett_2_col = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    col_2_lett = {v: k for k, v in lett_2_col.items()}
   
    def __init__(self,start, BOARD): 
        self.pstartRow = start[0]
        self.pstartCol = start[1]

    # this class will handle cases which happen before a player makes a move 
    
    def getGenLegalMov(self, matrix_dim):
        if self.pstartRow >= 0 and self.pstartRow < matrix_dim:
            return True
        else:
            return False


    def getLegMoveKnight(self):
        MATRIX_DIM = 8 
        self.possibleMoves = []
        moveLim = [(-1,-2),(-1,2),(-2,-1),(-2,1), (1,-2),( 1,2),( 2,-1),( 2,1)]

        for dif in moveLim:
            self.pstartRow = self.pstartRow + moveLim[0]
            self.pstartCol = self.pstartCol + moveLim[1]

            if self.getGenLegalMov(self.pstartRow, MATRIX_DIM) and self.getGenLegalMov(self.pstartCol, MATRIX_DIM):
                self.possibleMoves.append((self.pstartRow, self.pstartCol))
            
        return self.possibleMoves


    #     # we created a function that checks if the move is on the baord 

    #     pass

    # def getLegMoveKing(self): 
    #     pass

    # def getLegMoveQueen(self): 
    #     pass

    # def getLegMoveBishop(self): 
    #     pass

    # def getLegMovePawn(self): 
    #     pass

    # def getLegMovePawn(self): 
    #     #use heap for the double move




class Move():
     # switching to true row and column notation with dictionaries 

    num_2_row = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    row_2_num = {v: k for k, v in num_2_row.items()}
    lett_2_col = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    col_2_lett = {v: k for k, v in lett_2_col.items()}
   
    def __init__(self,start, end, BOARD): 
        self.startRow = start[0]
        self.startCol = start[1]
        self.endRow = end[0]
        self.endCol = end[1]
        self.PieceMoved = BOARD[self.startRow][self.startCol]
        self.PieceDed = BOARD[self.endRow][self.endCol]

    def getNotationFull(self):
        return self.get_lett(self.startRow, self.startCol) + self.get_lett(self.endRow, self.endCol)

    def getNotationStart(self): 
        return self.get_lett(self.startRow, self.startCol)

    def strNotation(self): 
        return print((self.get_lett(self.startRow, self.startCol), "->" , self.get_lett(self.endRow, self.endCol).encode()))
    
    def get_lett(self, row, col): 
        return self.col_2_lett[col] + self.row_2_num[row]



    

        
class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left_child = None
    self.right_child = None

def print_tree(node, level=0):
  if node:
    print_tree(node.right_child, level + 1)
    print(' ' * 4 * level + '->', node.value)
    print_tree(node.left_child, level + 1)

def insert(root, value):
  if root is None: # We cannot insert on an empty root. The root should exist first.
    return
  parent = None # We hold a pointer to the node that will be the parent of the new node we are inserting
  node = root # Also, we hold a pointer to traverse all the way through the path in which our new node will be inserted
  new_node = TreeNode(value) # Our new node to be inserted.
  while node is not None: # Keep traversing down until node is None. When that condition is met, parent will hold a pointer to the immediate previous node visited by the `node` variable, and thus, it will be the node where to hang our new node.
    parent = node
    if node.value > value: # If the value of the visited node is larger than our new value, then we should continue through the left subtree.
      node = node.left_child
    else: # Otherwise continue through the right subtree.
      node = node.right_child
  # We have found the parent of our new node:
  if parent.value > value: # If the value of the parent is larger than the new value, insert the new node at the left of `parent`
    parent.left_child = new_node
  else: # Otherwise, insert the new node at the right of the `parent`
    parent.right_child = new_node

def rcsearch(node, value):
  if not node:
    return
  if node.value == value:
    return node
  if node.value > value:
    return rcsearch(node.left_child, value)
  else:
    return rcsearch(node.right_child, value)

class button():
        
        #colours for button and text
 
        button_col = (255, 255, 255)
        hover_col = (75, 225, 255)
        click_col = (50, 150, 255)
        text_col = (0,0,0)
        width = 150
        height = 50
        WIDTH = 750
        HEIGHT = 900
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GREEN = (0, 102, 0)

        def __init__(self, x, y, text,screen):
            self.x = x
            self.y = y
            self.text = text
            self.screen = screen
            WIDTH = 750
            HEIGHT = 900
            BLACK = (0, 0, 0)
            WHITE = (255, 255, 255)
            GREEN = (0, 102, 0)
            self.BLACK = BLACK
            self.WHITE = WHITE
            self.GREEN = GREEN
            self.HEIGHT = HEIGHT
            self.WIDTH = WIDTH

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
            
            pg.draw.rect(self.screen, self.button_col, button_rect)
            
            #add shading to button
            pg.draw.line(self.screen, self.BLACK, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
            pg.draw.line(self.screen, self.BLACK, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

            #add text to button
            text_img = font.render(self.text, True, self.text_col)
            text_len = text_img.get_width()
            self.screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 18))
            return action

        def buttonColorManage(self,pos,undoButton,resetButton,quitButton,castleButton):
                if self.WIDTH //100 <= pos[0] <= self.WIDTH//100 + 150 and self.HEIGHT-self.HEIGHT//2.5 <= pos[1] <= self.HEIGHT-self.HEIGHT//2.5 + 50:
                    undoButton.button_col = (self.GREEN)
                    resetButton.button_col = (self.WHITE)
                    resetButton.draw_button()
                    quitButton.button_col = (self.WHITE)
                    quitButton.draw_button()
                    castleButton.button_col = (self.WHITE)
                    castleButton.draw_button()
                    undoButton.draw_button()
                elif self.WIDTH//100+170 <= pos[0] <= self.WIDTH//100+170 + 150 and self.HEIGHT-self.HEIGHT//2.5 <= pos[1] <=self.HEIGHT-self.HEIGHT//2.5 + 50:
                    resetButton.button_col = (self.GREEN)
                    undoButton.button_col = (self.WHITE)
                    undoButton.draw_button()
                    quitButton.button_col = (self.WHITE)
                    quitButton.draw_button()
                    castleButton.button_col = (self.WHITE)
                    castleButton.draw_button()
                    resetButton.draw_button()
                elif self.WIDTH//100+340 <= pos[0] <= self.WIDTH//100+340 + 215 and self.HEIGHT-self.HEIGHT//2.5 <= pos[1] <= self.HEIGHT-self.HEIGHT//2.5 + 50:
                    quitButton.button_col = (self.GREEN)
                    undoButton.button_col = (self.WHITE)
                    undoButton.draw_button()
                    resetButton.button_col = (self.WHITE)
                    resetButton.draw_button()
                    castleButton.button_col = (self.WHITE)
                    castleButton.draw_button()
                    quitButton.draw_button()

                elif self.WIDTH//100 <= pos[0] <= self.WIDTH//100 + 150 and self.HEIGHT-self.HEIGHT//2.5 + 70 <= pos[1] <= self.HEIGHT-self.HEIGHT//2.5 + 70 + 50:
                    castleButton.button_col = (self.GREEN)
                    undoButton.button_col = (self.WHITE)
                    undoButton.draw_button()
                    resetButton.button_col = (self.WHITE)
                    resetButton.draw_button()
                    quitButton.button_col = (self.WHITE)
                    quitButton.draw_button()
                    castleButton.draw_button()

                else:
                    undoButton.button_col = (self.WHITE)
                    undoButton.draw_button()
                    resetButton.button_col = (self.WHITE)
                    resetButton.draw_button()
                    quitButton.button_col = (self.WHITE)
                    quitButton.draw_button()
                    castleButton.button_col = (self.WHITE)
                    castleButton.draw_button()