mapping = {
    "q": "'",
    "w": ",",
    "e": ".",
    "r": "p",
    "t": "y",
    "y": "f",
    "u": "g",
    "i": "c",
    "o": "r",
    "p": "l",
    "a": "a",
    "s": "o",
    "d": "e",
    "f": "u",
    "g": "i",
    "h": "d",
    "j": "h",
    "k": "t",
    "l": "n",
    ";": "s",
    "z": ";",
    "x": "q",
    "c": "j",
    "v": "k",
    "b": "x",
    "n": "b",
    "m": "m",
    ",": "w",
    ".": "v",
    "/": "z",
    " ": " ",
}

answer = "odpoved je kamenice"

with open("keyboard_layout.txt", "w") as file:
    for char in answer:
        file.write(mapping[char])
