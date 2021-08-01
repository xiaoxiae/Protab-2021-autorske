from string import ascii_lowercase, ascii_uppercase


with open("input.txt") as f:
    contents = f.read()
    contents = contents.replace(".", " ")

    for c in ascii_lowercase + ascii_uppercase:
        contents = contents.replace(c, " ")

    print(contents)
