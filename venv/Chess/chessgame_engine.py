


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
            umove = self.movehistory.pop()
            self.BOARD[umove.startRow][umove.startCol] = umove.PieceMoved
            self.BOARD[umove.endRow][umove.endCol] = umove.PieceDed
            self.whiteMove = not self.whiteMove
            

    def ValidMoves(): 
        pass

    def AllPossibleMoves(self,whiteMove):
        for x in range(len(self.BOARD)):
            for y in range(len(self.BOARD[x])):
                if self.BOARD[x][y] != '--' and whiteMove:
                    print("WhitePeice on White Move")
                elif self.BOARD[x][y] != '--':
                    print("BlackPeice on BlackMove")
                else:
                    print("Not Applicable")
    

    #creating recommendation system using adjacency list and graphs
    
    def getGraph(self, move):
        piece = self.BOARD[move.startRow][move.StartCol]
        value_of_piece = None
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

    def getNotation(self):
        return self.get_lett(self.startRow, self.startCol) + self.get_lett(self.endRow, self.endCol)
    
    def get_lett(self, row, col): 
        return self.col_2_lett[col] + self.row_2_num[row]


    def getGenLegalMov(self, matrix_dim):
        if self.startRow >= 0 and self.startRow < matrix_dim:
            return True
        else:
            return False


    def getLegMoveKnight(self):
        MATRIX_DIM = 8 
        self.possibeMoves = []
        moveLim = [(-1,-2),(-1,2),(-2,-1),(-2,1), (1,-2),( 1,2),( 2,-1),( 2,1)]

        for dif in moveLim:
            self.pstartRow = self.startRow + moveLim[0]
            self.pstartCol = self.startCol + moveLim[1]

            if self.getGenLegalMove(self.pstartRow, MATRIX_DIM) and self.getGenLegalMov(self.pstartCol, MATRIX_DIM):
                self.possibleMoves.append((self.pstartRow, self.pstartCol))
            
        return self.possibeMoves


        # we created a function that checks if the move is on the baord 

        pass

    def getLegMoveKing(self): 
        pass

    def getLegMoveQueen(self): 
        pass

    def getLegMoveBishop(self): 
        pass

    def getLegMovePawn(self): 
        pass

    def getLegMovePawn(self): 
        pass


        
