with open("input_mini.txt") as f:
    maze = list(map(list, f.read().splitlines()))
    n = len(maze)
    total = 1
    maze[1][1] = "0"
    queue = [(1, 1, 1)]
    max = 0

    while len(queue) != 0:
        x, y, d = queue.pop(0)

        for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            nx, ny = x + dx, y + dy

            if nx < 0 or ny < 0 or nx >= len(maze) or ny >= len(maze):
                continue

            if maze[nx][ny] == " ":
                maze[nx][ny] = str(d)
                max = d

                queue.append((nx, ny, d + 1))

    print(max)

    with open("input_mini_out.txt", "w") as f:
        for line in maze:
            f.write("".join([(c if c not in ("#", " ") else ".").rjust(3, " ") for c in line]) + "\n")
