text = "input_1_en.txt"
password = "kopretina"

values = list(map(ord, open(text, "r").read().strip()))
coded_values = [
    value ^ ord(password[i % len(password)]) for i, value in enumerate(values)
]

open("xor1.txt", "w").write(
    f"Odpověď je české slovo délky {len(password)}.\n{str(coded_values)[1:-1]}"
)
