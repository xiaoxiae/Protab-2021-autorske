from random import *
from string import *
from subprocess import *

solution_added = False

def get_random_string(length=16):
    return "".join([choice(ascii_lowercase) for _ in range(length)])

def gen_recursive(depth, d_min_dec = 1, d_max_dec = 5, c_min=2, c_max=5):
    global solution_added

    name = get_random_string()
    if depth < 0:
        if not solution_added:
            Popen(["tar", "cfz", name + ".tar.gz", "heslo.txt"]).communicate()
            solution_added = True
        else:
            Popen(["tar", "cfz", name + ".tar.gz", "slepá ulička.txt"]).communicate()
        return name

    c_count = randint(c_min, c_max)
    d_decrease = randint(d_min_dec, d_max_dec)

    children = [gen_recursive(depth - d_decrease, d_min_dec, d_max_dec, c_min, c_max) for _ in range(c_count)]

    Popen(["tar", "cfz", name + ".tar.gz"] + list(map(lambda x: x + ".tar.gz", children))).communicate()
    Popen(["rm"] + list(map(lambda x: x + ".tar.gz", children))).communicate()

    return name

gen_recursive(14)
