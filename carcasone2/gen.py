from random import *

n = 3     # n**2 -- size of square
side = 4  # size of side

id_low, id_high = 1000, 9999

d = n * (side - 1) + 1

bits = tuple(tuple(randint(0, 1) for c in range(d)) for _ in range(d))

pieces = []
for x in range(0, n * (side - 1), side - 1):
    for y in range(0, n * (side - 1), side - 1):
        piece = ""
        for i in range(side):
            for j in range(side):
                piece = piece + str("#" if bits[x + i][y + j] == 0 else ".")
            piece = piece +"\n"
        pieces.append((randint(id_low, id_high), piece.strip()))

buffer = ""

for id, piece in pieces:
    buffer += f"""Tile {id}:
{piece}

"""

print(buffer.strip())
