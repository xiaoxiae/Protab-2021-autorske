"""Various utility function for getting input/printing the solution/..."""
import sys


def success(text):
    color = 2
    print(f"\u001b[38;5;{color}mResult: \u001b[0m{text}")
    sys.exit()


def get_input(as_int=False, whole=False):
    result = open("input", "r").read().strip()
    if not whole:
        result = result.splitlines()
    return list(map(int, result)) if as_int else result
