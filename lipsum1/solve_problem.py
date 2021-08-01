from random import choice

with open("problem.txt", "r") as file:
    paragraphs = file.read().splitlines()

coordinates = paragraphs[301:]

# parse each of the coordinates and reverse them
for coordinate in coordinates:
    char_str, row_str = coordinate.split(", ")

    print(paragraphs[int(char_str)][int(row_str)], end="")
