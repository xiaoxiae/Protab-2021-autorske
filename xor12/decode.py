text = open("xor1.txt", "r").read().splitlines()[1].split(",")

chars = "abcdefghijklmnopqrstuvwxyz"

for c1 in chars:
    for c2 in chars:
        for c3 in chars:
            password = c1 + c2 + c3

            decoded = []
            for i, string in enumerate(text):
                value = int(string.strip())

                decoded.append(chr(value ^ ord(password[i % 3])))

            spaces = decoded.count(" ")

            if spaces != 0 and len(decoded) / spaces < 8:
                print(password)
                print("".join(decoded))
                print()
