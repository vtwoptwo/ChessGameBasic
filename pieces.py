class Piece(object):
    def __init__(self, row, col, color = 0):
        self.row = row
        self.col = col
        self.color = color
        self.alive = True
        self.attacking = False
        self.moved = False

    def move(self, row, col):
        self.row = row
        self.col = col

    def kill(self):
        self.row = None
        self.col = None
        self.living = False

class King(Piece):
    def __init__(self, row, col, color = 0):
        super().__init__(row, col, color)
        self.piece = "King"

    def valid_move(self, row, col):
        r = abs(row - self.row)
        c = abs(col - self.col)

        if not (r <= 1 and c <= 1):
            return False
        return True

class Queen(Piece):
    def __init__(self, row, col, color = 0):
        super().__init__(row, col, color)
        self.piece = "Queen"

    def valid(self, row, col):
        r = abs(row - self.row)
        c = abs(col - self.col)

        if not (r == c or r == 0 or c == 0):
            return False
        return True

class Bishop(Piece):
    def __init__(self, row, col, color = 0):
        super().__init__(row, col, color)
        self.piece = "Bishop"

    def valid(self, row, col):
        r = abs(row - self.row)
        c = abs(col - self.col)

        if not (r == c):
            return False
        return True

class Rook(Piece):
    def __init__(self, row, col, color = 0):
        super().__init__(row, col, color)
        self.piece = "Rook"

    def valid(self, row, col):
        r = abs(row - self.row)
        c = abs(col - self.col)

        if not (r == 0 or c == 0):
            return False
        return True

class Knight(Piece):
    def __init__(self, row, col, color = 0):
        super().__init__(row, col, color)
        self.piece = "Knight"

    def valid(self, row, col):
        r = abs(row - self.row)
        c = abs(col - self.col)

        if not ((r == 2 and c == 1) or (r == 1 and c == 2)):
            return False
        return True

class Pawn(Piece):
    def __init__(self, row, col, color = 0):
        super().__init__(row, col, color)
        self.piece = "Pawn"

    def valid(self, row, col):
        bidirection = -2 * self.col + 3
        r = row - self.row
        c = col - self.col

        if (not self.attacking) and (not self.moved) and r == 0 and c == 2 * bidirection:
            return True
        elif self.attacking:
            if abs(r) == 1 and c == bidirection:
                return True
            else:
                return False
        elif not (r == 0 and c == bidirection):
            return False
        return True
