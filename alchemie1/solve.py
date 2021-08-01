from string import ascii_uppercase
from subprocess import *

input = """F je na sudé pozici
H je nalevo od D
A je 5 pozic od E
H je napravo od G
G je 3 pozice od C
F je napravo od C
D je na sudé pozici
C je na sudé pozici
E je nalevo od H
F je napravo od D
D je 2 pozice od C
B je nalevo od H"""

letters = sorted(list(set([c for c in input if c in ascii_uppercase])))
letters_string = ", ".join(letters)
n = len(letters)

rules = []

for line in input.split('\n'):
    if " je nalevo od " in line:
        a, b = line.split(" je nalevo od ")
        rules.append(f"{a} #=< {b}")
    elif " je napravo od " in line:
        a, b = line.split(" je napravo od ")
        rules.append(f"{a} #>= {b}")
    elif " je na sudé pozici" in line:
        a = line[0]
        rules.append(f"0 #= {a} mod 2")
    elif " je na liché pozici" in line:
        a = line[0]
        rules.append(f"1 #= {a} mod 2")
    elif "pozic" in line:
        a, rest = line.split(" je ")
        d, rest2 = rest.split("pozic")
        b = rest[-1]

        rules.append(f"({a} #= {b} + {d} ; {a} #= {b} - {d})")

rules_string = ", \n\t".join(rules)

result = f"""
?- use_module(library(clpfd)).

all_different_compounds({letters_string}) :-
	All = [{letters_string}],
	All ins 1..{n},
	all_distinct(All).

solve({letters_string}) :-
	all_different_compounds({letters_string}),
	{rules_string},
	All = [{letters_string}],
	label(All).

main() :- solve({letters_string}),
	{', print(" "), '.join('print(' + ascii_uppercase[i] + ')' for i in range(n))}.
    """

print(result)

with open("outsol.pl", "w") as f:
    f.write(result)

Popen(["swipl", "-o", "main", "-g", "main", "-c", "outsol.pl"], stdout=PIPE, stdin=PIPE).communicate()
result = Popen(["./main"], stdout=PIPE).communicate()[0].decode().strip().replace('"', '')
print(f"\n{result}\n")

