from pulp import *
from random import *
from itertools import *

n = 50

w = [randint(1, 1000) for _ in range(n)]

h = []
while sum(h) < sum(w):
    h.append(randint(1, 300))
h[-1] -= sum(h) - sum(w)

p_i, o_i, c_ij, l_ij = [
    w, h, [[randint(1, 1000) for _ in range(len(h))] for _ in range(len(w))], [[randint(1, 10000) for _ in range(len(h))] for _ in range(len(w))],
]

with open("p_i.txt", "w") as f:
    f.write((" ".join(map(str, p_i))))

with open("o_i.txt", "w") as f:
    f.write((" ".join(map(str, o_i))))

with open("c_ij.txt", "w") as f:
    for row in c_ij:
        f.write((" ".join(map(str, row))) + "\n")

with open("l_ij.txt", "w") as f:
    for row in c_ij:
        f.write((" ".join(map(str, [randint(1, c) for c in row]))) + "\n")
