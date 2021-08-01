text = open("xor2.txt", "r").read().splitlines()[1].split(",")

for password in open("czech.dic", "r").read().splitlines():
    if len(password) == 9:

        decoded = []
        for i, string in enumerate(text):
            value = int(string.strip())

            decoded.append(chr(value ^ ord(password[i % len(password)])))

        spaces = decoded.count(" ")

        if spaces != 0 and len(decoded) / spaces < 9:
            print(f"{password}: {''.join(decoded)}")
