from string import ascii_uppercase

with open("solution.txt") as f:
    x =list(map(int, f.read().strip().split()))
    result = [None] * len(x)
    print(x)

    for i, c in enumerate(ascii_uppercase[:len(x)]):
        result[x[i] - 1] = c
        
    print(x)
    print("".join(result))
