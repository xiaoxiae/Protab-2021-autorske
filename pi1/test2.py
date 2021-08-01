with open("output.txt") as f:
    numbers = list(map(int, f.read().strip().split()))

with open("pi1000000.txt") as f:
    pi = f.read().strip()

for number in numbers:
    print(chr(int(pi[number:number+2]) + ord('a') - 1))
    
