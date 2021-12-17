PIECES = {'bR': (3, "<Surface(62x62x32 SW)>"), 'bN': (4, "<Surface(62x62x32 SW)>"), 'bB': (5, "<Surface(62x62x32 SW)>"), 'bQ': (2, "<Surface(62x62x32 SW)>"), 'bK': (1, "<Surface(62x62x32 SW)>"), 'wB': (5, "<Surface(62x62x32 SW)>"), 'wN': (4, "<Surface(62x62x32 SW)>"), 'wR': (3, "<Surface(62x62x32 SW)>"), 'wQ': (2, "<Surface(62x62x32 SW)>"), 'wK': (1, "<Surface(62x62x32 SW)>"), 'bP': (6, "<Surface(62x62x32 SW)>"), 'wP': (6, "<Surface(62x62x32 SW)>")}

PIECESNUM = {}
for piece in PIECES:
    case = {PIECES[piece][0]: piece}
    PIECESNUM.update(case)
 

print(PIECESNUM)