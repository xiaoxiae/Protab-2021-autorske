area = []
pos = None
key_count = 0

# parse the area
for y, line in enumerate(open("inp", "r").read().strip().splitlines()):
    area.append([])
    for x, char in enumerate(line):
        # save start position
        if char == "@":
            pos = (x, y)
            char = " "

        area[-1].append(char)

# run BFS
stack = [(*pos, 0)]
explored = [[None for _ in range(len(area[0]))] for _ in range(len(area))]

while len(stack) != 0:
    x, y, steps = stack.pop(0)

    # check if we haven't already been here
    if explored[y][x] is not None:
        continue
    else:
        explored[y][x] = steps

    # for each direction
    for x_d, y_d in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        x_n, y_n = x + x_d, y + y_d

        # check out-of-bounds
        if x_n < 0 or x_n >= len(area[0]) or y_n < 0 or y_n >= len(area):
            continue

        char = area[y_n][x_n]

        # else if we're walking over empty space
        if char == " ":
            stack.append((x_n, y_n, steps + 1))

with open("tmp", "w") as f:
    for row in explored:
        f.write("\t".join([(str(c) if c else "/") for c in row]) + "\n")

print(steps - 1)
