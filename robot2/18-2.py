from itertools import product


def yield_sequences(area, pos):
    """Return the possible key/door sequences for collecting all keys in a given sector."""
    # count all the keys in the given sector (by running a regular BFS)
    stack = [pos]
    explored = [[False for _ in range(len(area[0]))] for _ in range(len(area))]
    key_count = 0

    while len(stack) != 0:
        x, y = stack.pop()

        # skip explored positions
        if explored[y][x]:
            continue

        explored[y][x] = True

        if 97 <= ord(area[y][x]) <= 122:
            key_count += 1

        for x_d, y_d in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            x_n, y_n = x + x_d, y + y_d

            if area[y_n][x_n] != "#":
                stack.append((x_n, y_n))

    # run the weird bfs and return all possible orders of keys-doors
    stack = [(*pos, 0, [], [])]
    explored = [[set() for _ in range(len(area[0]))] for _ in range(len(area))]

    while len(stack) != 0:
        x, y, steps, keys, sequence = stack.pop(0)

        # check if we haven't already been here
        key_tuple = tuple(keys)
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
                new_keys = list(keys)

                # possibly add the key
                if char not in new_keys:
                    new_keys.append(char)

                # if we've collected all keys, yield the key/door sequence
                if len(new_keys) == key_count:
                    yield steps + 1, sequence + [char]
                else:
                    stack.append((x_n, y_n, steps + 1, new_keys, sequence + [char]))

            # else if we're walking over empty space, continue BFS
            elif char == " ":
                stack.append((x_n, y_n, steps + 1, list(keys), sequence))

            # else if we're walking over a door, add it
            elif 65 <= ord(char) <= 90:
                stack.append((x_n, y_n, steps + 1, list(keys), sequence + [char]))


area = []
pos = None

# parse the area
for y, line in enumerate(open("input_", "r").read().strip().splitlines()):
    area.append([])
    for x, char in enumerate(line):
        # save the start position
        if char == "@":
            pos = (x, y)

        area[-1].append(char)

# build the blockage
area[pos[1]][pos[0]] = "#"
for x_d, y_d in ((0, 1), (1, 0), (-1, 0), (0, -1)):
    area[pos[1] + y_d][pos[0] + x_d] = "#"

# get all key/door sequences in all of the 4 corners
sequences = []
for x_d, y_d in ((-1, 1), (1, 1), (-1, -1), (1, -1)):
    sequences.append([s for s in yield_sequences(area, (pos[0] + x_d, pos[1] + y_d))])

print(sequences[:10])
quit()

# for each sequence quadruple, figure out if it is possible
minimum_steps = float("+inf")
for i, combination in enumerate(product(*sequences)):
    keys = set()
    positions = [0] * len(combination)

    # check, whether the combination is valid
    while True:
        was_changed = False

        for i, c in enumerate(combination):
            sequence = c[1]

            while positions[i] < len(sequence):
                # add keys to key set and increment the position
                if 97 <= ord(sequence[positions[i]]) <= 122:
                    keys.add(sequence[positions[i]])
                    positions[i] += 1
                    was_changed = True

                # check for keys to the door
                elif 65 <= ord(sequence[positions[i]]) <= 90:
                    if chr(ord(sequence[positions[i]]) + 32) not in keys:
                        break

                    # else continue through the door
                    positions[i] += 1

        # if we're stuck at doors, go to the next combination
        if not was_changed:
            break

        # if there are no more doors, evaluate the combination score
        for i, c in enumerate(combination):
            if positions[i] != len(c[1]):
                break
        else:
            # if all keys were collected, compare the steps to minimum steps
            steps = 0
            for score, _ in combination:
                steps += score

            if minimum_steps > steps:
                minimum_steps = steps
            break

print(minimum_steps)
