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

    def __str__(self):
        return f"<{self.values[0]}, {self.values[1]}, {self.values[2]}>"

    def sign(self):
        return Vector(*iter(1 if c > 0 else -1 if c < 0 else 0 for c in self))

    def abs(self):
        return Vector(*iter(abs(c) for c in self))


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

    def get_energy(self):
        p = 1
        for i in self.vel:
            p *= i
        return p


# parse file
moons = [
    Moon(Vector(*map(int, sub("[<>=xyz,]", "", pos).split(" "))))
    for pos in open("12.in", "r").read().strip().splitlines()
]

def simulate_moons():
    # gravitate
    for j, m1 in enumerate(moons):
        for _, m2 in enumerate(moons[j + 1 :]):
            m1.gravitate(m2)

    # move change accumulate velocity and move by it
    for m in moons:
        m.move()

# simulate moon movement
for i in range(10000):
    simulate_moons()

prod = 1
for m in moons:
    prod *= m.get_energy()

for m in moons:
    print(m.pos, m.vel)

print(prod)
