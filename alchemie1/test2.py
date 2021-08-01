from string import ascii_uppercase
from random import *
from subprocess import *

n = 8

letters = ascii_uppercase[:n]
letter_pool = letters

letters_string = ', '.join([ascii_uppercase[i] for i in range(n)])
numbers = [i + 1 for i in range(n)]

with open("solution.txt", "w") as f:
    f.write(str(numbers))

different_letters = [(u, v) for u in letters[:n] for v in letters[:n] if u != v and u in letter_pool or v in letter_pool]

shuffle(numbers)

def parity():
    v = choice(letter_pool)
    return (f"{v} je na {'sudé' if numbers[letters.index(v)] % 2 == 0 else 'liché'} pozici", f"{numbers[letters.index(v)] % 2} #= {v} mod 2")

def relation():
    u, v = choice(different_letters)
    return (f"{u} je {'napravo' if numbers[letters.index(u)] > numbers[letters.index(v)] else 'nalevo'} od {v}", f"{u} {'#>=' if numbers[letters.index(u)] > numbers[letters.index(v)] else '#=<'} {v}")

def distance():
    u, v = choice(different_letters)
    d = abs(numbers[letters.index(u)] - numbers[letters.index(v)])

    return (f"{u} je {d} pozic{'i' if d == 1 else 'e' if d in (2, 3, 4) else ''} od {v}", f"({u} #= {v} + {d}; {u} #= {v} - {d})")


rule_functions = [parity, relation, distance]
rules = []
rules_text = []
previous_result = [0 for i in range(n)]

while True:
    text, rule = choice(rule_functions)()

    rules.append(rule)
    rules_text.append(text)

    rules_string = ", \n\t".join(rules)
    rules_text_string = "\n".join([f"<li>{item}</li>" for item in rules_text])

    # incorrect letters
    letter_pool = [letter for i, letter in enumerate(letters) if previous_result[i] != numbers[i]]
    print(letter_pool)

    different_letters = [(u, v) for u in letters[:n] for v in letters[:n] if u != v and u in letter_pool or v in letter_pool]

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

    text = f"""<p>Pomíchaly se vám označení lahviček v laboratoři!</p>

<p>Lahvičky se nachází v řadě (na pozicích od {1} do {n}) a mají označení od {letters[0]} do {letters[-1]}.</p>

<p>Vaším cílem je pořadí jednoznačně určit, když víte následující:</p>

<ul>
{rules_text_string}
</ul>

<p>Řešení odevzdávejte jako čísla oddělená mezerou udávající pořadí láhviček {letters[0]}, {letters[1]},..., {letters[-1]}.</p>
"""

    with open("out.pl", "w") as f:
        f.write(result)

    with open("zadani.md", "w") as f:
        f.write(text)

    Popen(["swipl", "-o", "main", "-g", "main", "-c", "out.pl"], stdout=PIPE, stdin=PIPE).communicate()
    result = Popen(["./main"], stdout=PIPE).communicate()[0].decode().strip().replace('"', '')

    previous_result = list(map(int, result.split()))

    print(f"\n{result}\n")

