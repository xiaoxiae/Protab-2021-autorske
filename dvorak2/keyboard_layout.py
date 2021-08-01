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
    "'": "-",
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
    "-": "[",
    "[": "/",
}

answer = "heslo je tentokrat o trochu komplikovanejsi, a to tankodrom"

x = set()

for i in range(184):
    answer = "".join(map(lambda x: mapping[x], answer))
    print(answer)
    x.add(answer)

print(answer)
quit()

with open("keyboard_layout.txt", "w") as file:
    file.write(answer)
