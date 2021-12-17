import pygame as pg
from pygame.locals import *

# We would use this graph for our reccomendation system if we had more time as of right now it is not being used
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


# This is our main operating class, it keeps track of all our game operations
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

        #boolean value to indicate white or black move
        self.whiteMove = True

        # used for undoing moves
        self.movehistory = [] # implementation of a stack :) this can be used to undo a move 
                                #if we undo a move there actually needs to be an implementation of some 
                                #rules...movehistory, versus backtracking? does it count as a move? 
        # keeps track of taken pieces
        self.Zombies = []
        #our two heaps used for blitting a sorted list of captured pieces to the right side of the screen in order of value
        self.ZombiesBlack = Heap(16,max_heap)
        self.ZombiesWhite = Heap(16,max_heap)
        # helper dicationaries for operating with the heaps
        self.PIECESW = {}
        self.PIECESB = {}
    # where the two dictionaries above are filled to their relationships established
    def initialize_dicts(self, dict):
          for piece in dict:
              if piece[0] == 'w':
                  case = {dict[piece][0]: dict[piece][1]}
                  self.PIECESW.update(case)
              if piece[0] == 'b':
                  case = {dict[piece][0]: dict[piece][1]}
                  self.PIECESB.update(case)
    #keeps track of the updating of the heaps
    def updateHeaps(self,dict):
          self.ZombiesWhite.__init__(16,max_heap)
          self.ZombiesBlack.__init__(16,max_heap)
          for zombie in self.Zombies:
            number = dict[zombie][0]
            if zombie[0] == 'w':
              self.ZombiesWhite.insert(number)
            if zombie[0] == 'b':
              self.ZombiesBlack.insert(number)
          print("Pieces White: ",self.PIECESW)
          print("Pieces Black: ",self.PIECESB)
          print("White Data Heap: ",self.ZombiesWhite.data)
          print("Black Data Heap: ",self.ZombiesBlack.data)
          
    # draws dead pieces
    def drawZombies(self,screen, dict): 
        wp = 0
        bp = 0 
        for value in self.ZombiesWhite.data:
          print("Value White: ",value)
          if value != 0:
            whiteimg = self.PIECESW[value]
            screen.blit(whiteimg,(530, 50+wp))
            wp += 45
          else: continue


        for value in self.ZombiesBlack.data:
          print("Value Black: ",value)
          if value != 0:
            blackimg = self.PIECESB[value]
            screen.blit(blackimg,(570, 50+bp))
            bp += 45
          else: continue
          

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

    def undoMove(self, root):
        if len(self.movehistory) == 0:
            return # makes sure program doesnt crash if undo button is pressed and move history is empty
        else:
            if len(self.Zombies) != 0:
              self.Zombies.pop()
            umove = self.movehistory.pop()
            root.movesUndoTree(root,umove)
            self.BOARD[umove.startRow][umove.startCol] = umove.PieceMoved
            self.BOARD[umove.endRow][umove.endCol] = umove.PieceDed
            self.whiteMove = not self.whiteMove

    
    def getGraph(self, move, library):
        piece = self.BOARD[move.startRow][move.StartCol]
        if piece == "bN":                                                                  
            pass
            #for all node in all possible nodes that the knight can reach in one node
            #tempgraphforknight.add_vertex(node)
            #for node in all possiblenodes()
            # w = weight of each destination node extracted from the dictionary
            #tempgraphadd_edge(piece_node, node, w) 
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
    
    def getNotationBack(self):
      return self.get_lett(self.endRow, self.endCol) + self.get_lett(self.startRow, self.startCol)

    def strNotation(self): 
      return print((self.get_lett(self.startRow, self.startCol), "->" , self.get_lett(self.endRow, self.endCol).encode()))
    
    def get_lett(self, row, col):
      return self.col_2_lett[col] + self.row_2_num[row]



    

        
class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left_child = None
    self.right_child = None

  def print_tree(self,node, level=0):
    if node:
      self.print_tree(node.right_child, level + 1)
      print(' ' * 4 * level + '->', node.value)
      self.print_tree(node.left_child, level + 1)

  def insert(self,root,value):
    if root is None: 
      return
    parent = None 
    node = root 
    new_node = TreeNode(value) 
    while node is not None: 
      parent = node
      if node.value > value: 
        node = node.left_child
      else: 
        node = node.right_child
    
    if parent.value > value: 
      parent.left_child = new_node
    else: 
      parent.right_child = new_node

  def rcsearch(self,node,value):
    if not node:
      return
    if node.value == value:
      return node
    if node.value > value:
      return self.rcsearch(node.left_child, value)
    else:
      return self.rcsearch(node.right_child, value)

  def movesMadeTree(self,root, move):
    move_text = move.getNotationFull()
    self.insert(root, move_text)
    self.print_tree(root)
  
  def movesUndoTree(self,root, move): 
    umove_text = move.getNotationFull()
    self.remove(root, umove_text)
    self.print_tree(root)

  def inorder(self, root): 
    if root is None: 
      return

    self.inorder(root.left_child)
    print(root.value, end = '')
    self.inorder(root.right_child)


  def minValue(self, node):
    while(node.left_child is not None): 
      node = node.left_child
    return node

  def movesMadeTree(self,root, move):
    move_text = move.getNotationFull()
    self.insert(root, move_text)
    self.print_tree(root)

  def minValue(self,node):
          n = node
          while(n.left_child is not None): 
            n = n.left_child
          return n
  
  def remove(self,root, value):
     # Base Case
    if root is None:
        return root
 
    # Recursive calls for ancestors of
    # node to be deleted
    if value < root.value:
        root.left_child = self.remove(root.left_child, value)
        return root
 
    elif(value > root.value):
        root.right_child = self.remove(root.right_child, value)
        return root
     
    if root.left_child is None and root.right_child is None:
          return None
 
    if root.left_child is None:
        temp = root.right_child
        root = None
        return temp
 
    elif root.right_child is None:
        temp = root.left_child
        root = None
        return temp

    pParent = root
 
    pre_parent = root.right_child
 
    while pre_parent.left_child != None:
        pParent = pre_parent
        pre_parent = pre_parent.left_child
 
    if pParent != root:
        pParent.left_child = pre_parent.right_child
    else:
        pParent.right_child = pre_parent.right_child
 
    root.value = pre_parent.value
 
    return root
    
class Heap:
  def __init__(self, max_size, priority_func):
    self.data = [0] * max_size 
    self.item_count = 0 
    self.max_size = max_size 
    self.priority = priority_func
    
  def parent_index(self, i):
    return ((i + 1) // 2) - 1
    
  def left_child_index(self, i):
    return 2 * (i + 1) - 1
    
  def right_child_index(self, i):
    return 2 * (i + 1)
    
  def insert(self, value):
    if self.item_count == self.max_size: 
      return
    self.data[self.item_count] = value 
    self.bubble_up(self.item_count) 
    self.item_count += 1 

  def extract(self):
    if self.item_count == 0: 
      return
    value = self.data[0] 
    self.item_count -= 1
    self.data[0] = self.data[self.item_count] # Move the last element to the root of the heap
    self.bubble_down(0) # And then, make it bubble down while its priority is lower than that of its children
    self.data[self.item_count] = 0 # Clear the last element. This is not necessary, since this index shall be overriden upon the next insertion.
    return value
    
  def bubble_up(self, i):
    parent = self.parent_index(i)
    while parent >= 0: # While we do not overpass the root index.
      if self.priority(self.data[parent], self.data[i]) < 0: # If the element at `i` has a higher priority than its parent, swap them.
        self.data[parent], self.data[i] = self.data[i], self.data[parent]
        # This part was missing from the class session: we need to keep on bubling up, so we readjust the parent and child pointers
        i = parent # Continue with the grandparent, that is now the parent
        parent = self.parent_index(i)
      else:
        break

        
  def bubble_down(self, i):
    while self.left_child_index(i) < self.item_count: # While we do not overpass the last item of our Heap
      # Get the indices of the left and right children of `i`
      right_child = self.right_child_index(i)
      left_child = self.left_child_index(i)
      if right_child >= self.item_count: # In this case, the righ_child index overpass the last item, so it means there is no right child.
        child = left_child # So the item to compare the parent against, this is `child`, is the left_child.
      elif self.priority(self.data[left_child], self.data[right_child]) > 0: # Now select the child with the highest priority of the two.
        child = left_child
      else:
        child = right_child
      if self.priority(self.data[i], self.data[child]) >= 0: # If the parent has a higher priority than its children, then we stop iterating, since the priority hierarchy is respected.
        return
      self.data[i], self.data[child] = self.data[child], self.data[i] # Else, swap parent and child, and keep iterating all the way down.
      i = child


def max_heap(x, y):
  return x - y

def min_heap(x, y):
  return y - x
      

class button():
        
        #colours for button and text and other attributes
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

        # init for button
        def __init__(self, x, y, text,screen):
            self.x = x
            self.y = y
            self.text = text
            self.screen = screen
            #this kind of strange init part is so the button management is performed in the engine
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
        
        #this code is allowing the buttons to change colors when the mouse highlights over them, nice UI addition
        # kind of costly for effeciency but for the user adds significantly
        # much like the click locations these intervals just define where the mouse needs to be for the button to turn gree or white respectively 
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