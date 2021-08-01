from random import *

n = 500

maze = []
for i in range(n):
    maze.append([])
    for j in range(n):
        maze[-1].append(0 if random() < 0.79 else 1)

def at(n, maze, x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return 0
    return maze[x][y]

iterations = 4
for _ in range(iterations):
    new_maze = [list(row) for row in maze]

    for i in range(n):
        for j in range(n):
            total = 0
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)):
                total += at(n, maze, i + dx, j + dy)

            new_maze[i][j] = 0 if total <= 2 else 1

    maze = new_maze

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n - 1 or j == n - 1:
            maze[i][j] = 1

with open("input.txt", "w") as f:
    for row in maze:
        f.write("".join(map(lambda x: " " if x == 0 else "#", row)) + "\n")
