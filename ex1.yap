node(1).
node(2).
node(3).
node(4).
edge(1, 2).
edge(2, 4).
edge(4, 3).
edge(3, 2).
edge(1, 4).
route(A, B) :- edge(A, B).
route(A, B) :- 
	edge(A, C),  
	route(C, B).

travel(A, B, P, [B | P]) :- edge(A, B).

travel(A, B, Visited, Path) :-
	edge(A, C),
	C \== B,
		\+member(C, Visited),
		travel(C, B, [C | Visited], Path)
.

append([H | T], L, [H | R]) :- 
	append(T, L, R)
.

append([], L, L).

reverse([H | T], X) :-
	reverse(T, Y),
	append(Y, [H], X)
.

reverse([], []).

path(A, B, Path) :-
	travel(A, B, [A], Q),
	reverse(Q, Path)
.