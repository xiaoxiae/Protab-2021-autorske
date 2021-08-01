import sys

sys.path.insert(0, "../")
from utilities import success, get_input
from typing import *

from itertools import product

input = get_input(whole=True)

images = set()

for image in input.split("\n\n"):
    id = int(image.split("\n")[0].split(" ")[1].strip(":"))

    images.add((id, tuple(image.split("\n")[2:])))

def yield_symmetric_images(image):
    """Yield the possible rotations of the image."""
    for h in (True, False):  # horizontal
        for v in (True, False):  # vertical
            for d in (True, False):  # diagonal
                new_image = list(image)

                if v:
                    new_image = list(reversed(new_image))

                if h:
                    new_image = [row[::-1] for row in new_image]

                if d:
                    new_image = [
                        "".join([new_image[c][r] for c in range(len(new_image))])
                        for r in range(len(new_image))
                    ]

                yield tuple(new_image)


def down(i1, i2):
    """Return True if the image i2 can be below i1."""
    return i1[-1] == i2[0]


def right(i1, i2):
    """Return True if the image i2 can be to the right of i1."""
    return "".join([i1[row][-1] for row in range(len(i1))]) == "".join(
        [i2[row][0] for row in range(len(i2))]
    )

total = 0

def fill(square, images, current: int):
    global total

    if current == len(square) ** 2:
        print("found")
        total += 1
        return

    x, y = current % len(square), current // len(square)

    for id, image in images:

        for symmetric_image in yield_symmetric_images(image):

            # if we can add it
            if (y == 0 or down(square[y - 1][x][1], symmetric_image)) and (
                x == 0 or right(square[y][x - 1][1], symmetric_image)
            ):

                square[y][x] = (id, symmetric_image)
                fill(square, images - {(id, image)}, current + 1)
                square[y][x] = None


side = int(len(images) ** (1 / 2))

result = fill([[None] * side for _ in range(side)], images, 0)

print(total / 8)
