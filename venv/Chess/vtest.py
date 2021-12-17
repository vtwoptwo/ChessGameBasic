PIECES = {'bR': (3, "<Surface(62x62x32 SW)>"), 'bN': (4, "<Surface(62x62x32 SW)>"), 'bB': (5, "<Surface(62x62x32 SW)>"), 'bQ': (2, "<Surface(62x62x32 SW)>"), 'bK': (1, "<Surface(62x62x32 SW)>"), 'wB': (5, "<Surface(62x62x32 SW)>"), 'wN': (4, "<Surface(62x62x32 SW)>"), 'wR': (3, "<Surface(62x62x32 SW)>"), 'wQ': (2, "<Surface(62x62x32 SW)>"), 'wK': (1, "<Surface(62x62x32 SW)>"), 'bP': (6, "<Surface(62x62x32 SW)>"), 'wP': (6, "<Surface(62x62x32 SW)>")}
HASHPIECESW = []
HASHPIECESB = []


def str_to_number(string):
  number = 0
  # A string in python is just a list of characters, with extra functions built around. So we can iterate over it using the index of each character.
  # We will use then the index of each character to compose the exponent to which we have to raise the base, 128, for each of them.
  for i in range(len(string)): 
    exponent = len(string) - 1 - i # Exponents start at len(string) - 1, and decrease one by one upt to 0.
    asc = ord(string[i]) # Compute the ascii number corresponding to that character at position i.
    number += asc * (128**exponent) # Calculate the base-128 for this character at position i, and accumulate it in number
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