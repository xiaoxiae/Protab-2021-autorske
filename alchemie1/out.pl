
?- use_module(library(clpfd)).

all_different_compounds(A, B, C, D, E, F, G, H) :-
	All = [A, B, C, D, E, F, G, H],
	All ins 1..8,
	all_distinct(All).

solve(A, B, C, D, E, F, G, H) :-
	all_different_compounds(A, B, C, D, E, F, G, H),
	0 #= F mod 2, 
	H #=< D, 
	(A #= E + 5; A #= E - 5), 
	H #>= G, 
	(G #= C + 3; G #= C - 3), 
	F #>= C, 
	0 #= D mod 2, 
	0 #= C mod 2, 
	E #=< H, 
	F #>= D, 
	B #=< H, 
	(D #= C + 2; D #= C - 2),
	All = [A, B, C, D, E, F, G, H],
	label(All).

main() :- solve(A, B, C, D, E, F, G, H),
	print(A), print(" "), print(B), print(" "), print(C), print(" "), print(D), print(" "), print(E), print(" "), print(F), print(" "), print(G), print(" "), print(H).
    
