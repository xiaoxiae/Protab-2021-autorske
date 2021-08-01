from string import ascii_uppercase
from subprocess import *

input = """J je na liché pozici
M je 8 pozic od I
D je na liché pozici
P je na sudé pozici
A je 2 pozice od C
O je 9 pozic od Y
A je na sudé pozici
L je 4 pozice od A
I je na sudé pozici
E je na liché pozici
K je 9 pozic od P
R je nalevo od U
K je 8 pozic od D
O je 5 pozic od H
T je na sudé pozici
T je 10 pozic od H
U je 17 pozic od W
S je na sudé pozici
G je na liché pozici
I je napravo od W
D je napravo od S
X je 19 pozic od L
U je napravo od C
G je 5 pozic od B
P je napravo od N
F je 15 pozic od Y
M je na sudé pozici
G je napravo od Q
E je 16 pozic od N
Y je na sudé pozici
Q je 3 pozice od C
J je napravo od S
L je 1 pozici od Q
Y je nalevo od X
H je 12 pozic od I
Q je nalevo od J
B je na sudé pozici
S je nalevo od X
R je nalevo od G
T je 6 pozic od B
Q je na liché pozici
E je 4 pozice od U
E je napravo od H
R je napravo od V"""

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

