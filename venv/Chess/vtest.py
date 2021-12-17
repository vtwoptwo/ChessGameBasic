PIECES = {'bR': (3, "<Surface(62x62x32 SW)>"), 'bN': (4, "<Surface(62x62x32 SW)>"), 'bB': (5, "<Surface(62x62x32 SW)>"), 'bQ': (2, "<Surface(62x62x32 SW)>"), 'bK': (1, "<Surface(62x62x32 SW)>"), 'wB': (5, "<Surface(62x62x32 SW)>"), 'wN': (4, "<Surface(62x62x32 SW)>"), 'wR': (3, "<Surface(62x62x32 SW)>"), 'wQ': (2, "<Surface(62x62x32 SW)>"), 'wK': (1, "<Surface(62x62x32 SW)>"), 'bP': (6, "<Surface(62x62x32 SW)>"), 'wP': (6, "<Surface(62x62x32 SW)>")}
HASHPIECESW = []
HASHPIECESB = []


def str_to_number(string):
  number = 0
  for i in range(len(string)):
    exponent = len(string) - 1 - i
    asc = ord(string[i]) 
    number += asc * (128**exponent)
  return number


for piece in PIECES:
    if piece[0] == 'w':
        case = (piece + str(PIECES[piece][0]))
        hase = str_to_number(case)
        HASHPIECESW.append(hase)
    if piece[0] == 'b':
        case = (piece + str(PIECES[piece][0]))
        hase = str_to_number(case)
        HASHPIECESB.append(hase)


print(HASHPIECESB)
print(HASHPIECESW)