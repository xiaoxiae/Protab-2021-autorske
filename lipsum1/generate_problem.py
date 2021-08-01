from random import choice


def get_char(paragraphs, i, j):
    """Return the j-th character from the i-th paragraph (or None)."""
    if i < len(paragraphs) and j < len(paragraphs[i]):
        return paragraphs[i][j]
    else:
        return None


with open("lipsum.txt", "r") as file:
    paragraphs = file.read().splitlines()

# the fake and the real sentences that will be hidden in the text
fake_sentence = "hledej trochu jinde"
real_sentence = "odpoved je maturita"

transformations = list(zip(fake_sentence, real_sentence))
transformation_indexes = [[] for _x in range(len(transformations))]

# go through every transformation
for i in range(len(transformations)):
    # transform from character to character
    transform_from = transformations[i][0]
    transform_to = transformations[i][1]

    for j in range(len(paragraphs)):
        for k in range(len(paragraphs[j])):
            # if both of the transformations match
            if get_char(paragraphs, j, k) == transform_from:
                if get_char(paragraphs, k, j) == transform_to:
                    # add them to the list of transformations
                    transformation_indexes[i].append((j, k))

# if transformations for some words don't exist, exit
for t in transformation_indexes:
    if len(t) == 0:
        print("Transformation mismatch, no problem was generated.")
        quit()

with open("problem.txt", "w") as file:
    # first write the lipsum
    for paragraph in paragraphs:
        file.write(paragraph + "\n")
    file.write("\n")

    # then randomly write the transformations
    for t in transformation_indexes:
        selected_t = choice(t)

        file.write("%i, %i\n" % (selected_t[0], selected_t[1]))
