from pulp import *
from itertools import *

with open("p_ii.txt") as f:
    p = list(map(int, f.read().split()))

with open("o_ii.txt") as f:
    o = list(map(int, f.read().split()))

c = []
with open("c_ijj.txt") as f:
    for line in f.read().splitlines():
        c.append(list(map(int, line.split())))

l = []
with open("l_ijj.txt") as f:
    for line in f.read().splitlines():
        l.append(list(map(int, line.split())))

# počet pekáren, počet obchodů
n = len(p)
m = len(o)

# vytvoření modelu
model = LpProblem(name="1-a", sense=LpMinimize)

# proměnné -- x_{ij}, kolik i-tá pekárna doveze j-tému obchodu
# proměnné jsou celočíselné a nezáporné
x = []
for i in range(n):
    x.append([])
    for j in range(m):
        x[-1].append(LpVariable(name=f"x_{i}_{j}", lowBound=0, cat='Integer'))

# proměnné -- xl_{ij}, zda počítáme pro daný spoj náklady
# proměnné jsou celočíselné a nezáporné
xl = []
for i in range(n):
    xl.append([])
    for j in range(m):
        xl[-1].append(LpVariable(name=f"xl_{i}_{j}", lowBound=0, cat='Binary'))

# omezení
## každá pekárna rozveze všechny rohlíky
for i in range(n):
    model += p[i] == lpSum([x[i][j] for j in range(m)])

## každý obchod získá potřebné rohlíky
for i in range(m):
    model += o[i] == lpSum([x[j][i] for j in range(n)])

## donucení transportu, když dovážíme nějaké rohlíky
# trik s tím, že je to níže nulové, když x_i_j je nulové, a jindy kladné reálné menší než 1
for i in range(n):
    for j in range(m):
        model += xl[i][j] >= x[i][j] * (1 / p[i])

# funkce k minimalizaci -- náklady
model += lpSum([x[i][j] * c[i][j] for i in range(n) for j in range(m)] \
        + [xl[i][j] * l[i][j] for i in range(n) for j in range(m)])

# řešení (ignorujeme debug zprávy)
status = model.solve(PULP_CBC_CMD(msg=False))

print("náklady:", int(model.objective.value()))
