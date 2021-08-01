from random import *

result = "odpovednatentoproblemjeslovolevandule"

with open("pi1000000.txt") as f:
    pi = f.read().strip()

digit_positions = {
    f"{a+1:02}" :[] for a in range(26)
}

for i in range(len(pi) - 1):
    part = pi[i:i+2]
    if part in digit_positions:
        digit_positions[part].append(i)

indexes = []
for char in result:
    indexes.append(choice(digit_positions[f"{ord(char) - ord('a') + 1:02}"]))

print(" ".join(map(str, indexes)))
