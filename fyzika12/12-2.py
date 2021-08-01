from __future__ import annotations
from dataclasses import dataclass
from typing import *

from re import sub


class Vector:
    values = None

    def __init__(self, *args):
        self.values = list(args)

    def __add__(self, other):
        return Vector(*iter(u + v for u, v in zip(self, other)))

    def __sub__(self, other):
        return Vector(*iter(u - v for u, v in zip(self, other)))

    def __getitem__(self, i):
        return self.values[i]

    def sign(self):
        return Vector(*iter(1 if c > 0 else -1 if c < 0 else 0 for c in self))


@dataclass
class Moon:
    pos: Vector
    vel: Vector = Vector(0, 0, 0)

    def gravitate(self, other: Moon):
        gravitational_force = (other.pos - self.pos).sign()

        self.vel += gravitational_force
        other.vel -= gravitational_force

    def move(self):
        self.pos += self.vel


def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


# parse file
moons = [
    Moon(Vector(*map(int, sub("[<>=xyz,]", "", pos).split(" "))))
    for pos in open("12.in", "r").read().strip().splitlines()
]

# separate tracking of the x, y, z positions + their velocities
position_history = [dict(), dict(), dict()]
steps = [-1, -1, -1]

# simulate moon movement, until we haven't found cycles for all the x, y, z coordinates
i = 0
while -1 in steps:
    # calculate x, y, z separately
    for j in range(3):
        # only calculate it if the loop hasn't been found yet
        if steps[j] == -1:
            p = tuple((m.pos[j], m.vel[j]) for m in moons)

            if p in position_history[j]:
                steps[j] = i
                print(p)
            else:
                position_history[j][p] = i

    # gravitate
    for j, m1 in enumerate(moons):
        for _, m2 in enumerate(moons[j + 1 :]):
            m1.gravitate(m2)

    # move change accumulate velocity and move by it
    for m in moons:
        m.move()

    i += 1

# calculate the LCM of the three numbers
tmp = (steps[0] * steps[1]) // gcd(steps[0], steps[1])
print((tmp * steps[2]) // gcd(tmp, steps[2]))
