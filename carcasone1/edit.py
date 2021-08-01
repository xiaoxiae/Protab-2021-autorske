def edit_tile(tile):
    tile = "Dílek " + tile[5:9] + "\n----------\n" + tile[10:].strip()

    lines = tile.split("\n")

    for i in range(3, len(lines) - 1):
        lines[i] = lines[i][:1] + ' ' * (len(lines[i]) - 2) + lines[i][-1:]

    tile = "\n".join(lines)
    tile = tile.replace(".", "0")
    tile = tile.replace("#", "1")

    return tile


with open('input.txt', "r") as f:
    tiles = f.read().split("\n\n")

print("\n\n".join([edit_tile(tile) for tile in tiles]))
