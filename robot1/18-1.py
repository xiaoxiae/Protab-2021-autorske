area = []
pos = None
key_count = 0

# parse the area
for y, line in enumerate(open("input", "r").read().strip().splitlines()):
    area.append([])
    for x, char in enumerate(line):
        # save start position
        if char == "@":
            pos = (x, y)
            char = " "

        # count the number of keys
        elif 97 <= ord(char) <= 122:
            key_count += 1

        area[-1].append(char)

# run BFS
stack = [(*pos, 0, set())]
explored = [[set() for _ in range(len(area[0]))] for _ in range(len(area))]

while len(stack) != 0:
    x, y, steps, keys = stack.pop(0)

    # check if we haven't already been here
    key_tuple = tuple(sorted(keys))
    if key_tuple in explored[y][x]:
        continue
    else:
        explored[y][x].add(key_tuple)

    # for each direction
    for x_d, y_d in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        x_n, y_n = x + x_d, y + y_d

        # check out-of-bounds
        if x_n < 0 or x_n >= len(area[0]) or y_n < 0 or y_n >= len(area):
            continue

        char = area[y_n][x_n]

        # if we're walking over a key, add it to the keys set
        if 97 <= ord(char) <= 122:
            new_keys = set(keys).union(char)

            if len(new_keys) == key_count:
                print(steps + 1)
                exit()
            else:
                stack.append((x_n, y_n, steps + 1, new_keys))

        # else if we're walking over empty space or unlocked door, continue
        elif char == " " or (65 <= ord(char) <= 90 and char.lower() in keys):
            stack.append((x_n, y_n, steps + 1, set(keys)))

