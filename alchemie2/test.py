from string import ascii_uppercase
from random import *
from subprocess import *

n = 15
m = 30

letters = ', '.join([ascii_uppercase[i] for i in range(n)])


odd_even_pool = list(ascii_uppercase)
shuffle(odd_even_pool)

left_right_next_pool = [(u, v) for u in ascii_uppercase for v in ascii_uppercase if u != v]
shuffle(left_right_next_pool)

print(left_right_next_pool)


def even():
    if len(odd_even_pool) == 0:
        return "true"
    return f"0 #= {odd_even_pool.pop()} mod 2"

def odd():
    if len(odd_even_pool) == 0:
        return "true"
    return f"1 #= {odd_even_pool.pop()} mod 2"

def left_to():
    u, v = left_right_next_pool.pop()
    if (v, u) in left_right_next_pool:
        left_right_next_pool.remove((v, u))
    return f"{u} #>= {v}"

def right_to():
    u, v = left_right_next_pool.pop()
    if (v, u) in left_right_next_pool:
        left_right_next_pool.remove((v, u))
    return f"{u} #=< {v}"

def next_to():
    u, v = left_right_next_pool.pop()
    if (v, u) in left_right_next_pool:
        left_right_next_pool.remove((v, u))
    return f"({u} #= {v} - 1; {u} #= {v} + 1)"

print(next_to())
quit()

rule_functions = [even, odd, left_to, right_to, next_to]
rules = [choice(rule_functions)() for _ in range(m)]

rules_string = ", \n\t".join(rules)

print(rules_string)

result = f"""
?- use_module(library(clpfd)).

all_different_compounds({letters}) :-
	All = [{letters}],
	All ins 1..{n},
	all_distinct(All).

solve({letters}) :-
	all_different_compounds({letters}),
	{rules_string},
	All = [{letters}],
	label(All).

main() :- solve({letters}),
    {', print(" "), '.join('print(' + ascii_uppercase[i] + ')' for i in range(n))}.
"""

with open("out.pl", "w") as f:
    f.write(result)

Popen(["swipl", "-o", "main", "-g", "main", "-c", "out.pl"], stdout=PIPE, stdin=PIPE).communicate()
result = Popen(["./main"], stdout=PIPE).communicate()[0].decode().strip().replace('"', '')
print(result)
