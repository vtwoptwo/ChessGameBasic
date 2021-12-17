

TIME COMPLEXITIES

Data Structures: 

DS A: MATRIX
for the matrix we actually change positions of pieces by having a time complexity of o(1)
we take the x and y value separate for each predefined quare in the matrix and and can thus manipulate 
piece movements in O(1) time

DS B:  BINARY SEARCH TREE

this datas structure was created to check if a king or rook has been moved or not in order to 
implement a "castling functionality"

we managed to tdo this with one of the kings 

due to tiume constraints we were unable to do it for both sides of each color, but the king for each color castles with the rook closest to him 



DS C: HEAP
the heap was created in order to apply a bubble sorting algorithm 
we ran into a few bugs once implemeing the heap but we think that with more time this would have been a problem which was easy to solve 

in fact we recognize that we should have used a hash function to identify the pieces, 

to be honest we had already created the hash function and were doing this 
but later decided against it

below you can see our implementation of the hash function 


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
