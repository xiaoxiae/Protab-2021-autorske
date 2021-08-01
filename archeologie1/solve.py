def dfs(maze, x, y, i):
    maze[x][y] = str(i)

    for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        nx, ny = x + dx, y + dy

        if nx < 0 or ny < 0 or nx >= len(maze) or ny >= len(maze):
            continue

        if maze[nx][ny] == " ":
            dfs(maze, nx, ny, i)


with open("input.txt") as f:
    maze = list(map(list, f.read().splitlines()))
    n = len(maze)
    total = 0

    for i in range(n):
        for j in range(n):
            if maze[i][j] == " ":
                dfs(maze, i, j, total)
                total += 1

    print(total)
