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
        self.ZombiesBlack = Heap(16,max_heap)
        self.ZombiesWhite = Heap(16,max_heap)
        self.PIECESW = {}
        self.PIECESB = {}
        self.ZombiesWhite = Heap(16,max_heap)
        self.ZombiesBlack = Heap(16,max_heap)
     
    def initialize_dicts(self, dict):
          for piece in dict:
              if piece[0] == 'w':
                  case = {dict[piece][0]: dict[piece][1]}
                  self.PIECESW.update(case)
              if piece[0] == 'b':
                  case = {dict[piece][0]: dict[piece][1]}
                  self.PIECESB.update(case)
      
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
 
    # We reach here when root is the node
    # to be deleted.
     
    # If root node is a leaf node
     
    if root.left_child is None and root.right_child is None:
          return None
 
    # If one of the children is empty
 
    if root.left_child is None:
        temp = root.right_child
        root = None
        return temp
 
    elif root.right_child is None:
        temp = root.left_child
        root = None
        return temp
 
    # If both children exist
 
    pParent = root
 
    # Find Successor
 
    pre_parent = root.right_child
 
    while pre_parent.left_child != None:
        pParent = pre_parent
        pre_parent = pre_parent.left_child
 
    # Delete successor.Since successor
    # is always left_child child of its parent
    # we can safely make successor's right_child
    # right_child child as left_child of its parent.
    # If there is no pre_parent, then assign
    # pre_parent->right_child to pParent->right_child
    if pParent != root:
        pParent.left_child = pre_parent.right_child
    else:
        pParent.right_child = pre_parent.right_child
 
    # Copy Successor Data to root
 
    root.value = pre_parent.value
 
    return root
    
class Heap:
  def __init__(self, max_size, priority_func):
    self.data = [0] * max_size # Initialize our data container array. It will be an array of size `max_size`, with all its values zeroed.
    self.item_count = 0 # The next empty slot where to insert new elements
    self.max_size = max_size # Keep the max_size as an upper bound for out Heap
    self.priority = priority_func # The priority function to decide which of two elements has the higest priority.
    
  def parent_index(self, i):
    return ((i + 1) // 2) - 1
    
  def left_child_index(self, i):
    return 2 * (i + 1) - 1
    
  def right_child_index(self, i):
    return 2 * (i + 1)
    
  def insert(self, value):
    if self.item_count == self.max_size: # Heap Overflow. Do not insert if the Heap is full
      return
    self.data[self.item_count] = value # Store the new element at the next empty spot.
    self.bubble_up(self.item_count) # Then, make it bubble up while its priority is higher than that of its parents.
    self.item_count += 1 

  def extract(self):
    if self.item_count == 0: # Heap Underflow. We cannot extract from the heap if it's empty.
      return
    value = self.data[0] # The root of our heap is at pos 0 of our data array
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