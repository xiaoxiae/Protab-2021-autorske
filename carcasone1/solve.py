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


def fill(square, images, current: int):
    if current == len(square) ** 2:
        n = len(square)
        print([[column[0] for column in row] for row in square])
        print(square[n // 2][n // 2][0], square[n // 2][n // 2 - 1][0], square[n // 2 - 1][n // 2][0], square[n // 2 - 1][n // 2 - 1][0])
        success(square[n // 2][n // 2][0] + square[n // 2][n // 2 - 1][0] + square[n // 2 - 1][n // 2][0] + square[n // 2 - 1][n // 2 - 1][0])
        quit()

    x, y = current % len(square), current // len(square)

    for id, image in images:

        for symmetric_image in yield_symmetric_images(image):

            # if we can add it
            if (y == 0 or down(square[y - 1][x][1], symmetric_image)) and (
                x == 0 or right(square[y][x - 1][1], symmetric_image)
            ):

                #if square[0][0] is not None and square[0][0][0] == 1951:
                #    print(symmetric_image)

                square[y][x] = (id, symmetric_image)
                fill(square, images - {(id, image)}, current + 1)
                square[y][x] = None


side = int(len(images) ** (1 / 2))

result = fill([[None] * side for _ in range(side)], images, 0)
