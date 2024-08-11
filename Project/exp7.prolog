Prolog is a logic programming language that is particularly well-suited for representing and querying facts
and rules. Below, I'll provide a simple example using Prolog to represent facts and queries.

___________________________________________________________________________________________________________________________

```prolog
% Facts
mammal(horse).
mammal(dog).
bird(sparrow).
bird(penguin).
reptile(snake).
insect(bee).
fish(salmon).
% Queries
?- mammal(horse). % true
?- bird(penguin). % true
?- mammal(sparrow). % false
?- reptile(X). % X = snake (prolog will backtrack to find all reptiles)
```
===========================================================================================================================

In this Prolog code:
- Facts are represented using predicates like `mammal/1`, `bird/1`, etc.
- Queries are questions asked to Prolog about the facts.
Here's a brief explanation:
1. `mammal(horse).`: Asserts that a horse is a mammal.
2. `bird(sparrow).`: Asserts that a sparrow is a bird.
3. `?- mammal(horse).`: Asks if a horse is a mammal. Prolog will respond with `true`.
4. `?- bird(penguin).`: Asks if a penguin is a bird. Prolog will respond with `true`.
5. `?- mammal(sparrow).`: Asks if a sparrow is a mammal. Prolog will respond with `false`.
6. `?- reptile(X).`: Asks for a reptile. Prolog will respond with `X = snake`, and if you press `;` (semicolon),
it will backtrack to find all reptiles.
This is a very simple example, but Prolog is capable of handling more complex rules, relationships, and
queries. It excels in scenarios where logical reasoning and rule-based systems are required.

============================================================================================================================

Output:
PROLOG Solution done on Latex provides the following Solution:
1. `?- mammal(horse).` results in `true`.
2. `?- bird(penguin).` results in `true`.
3. `?- mammal(sparrow).` results in `false`.
4. `?- reptile(X).` results in `X = snake`.

============================================================================================================================

%Demonstration of Family tree using Prolog using conditional statements.

```prolog
% Facts
parent(john, jim).
parent(john, ann).
parent(susan, jim).
parent(susan, ann).
parent(jim, tom).
parent(ann, emily).
% Rules
father(Father, Child) :- parent(Father, Child), male(Father).
mother(Mother, Child) :- parent(Mother, Child), female(Mother).
grandparent(Grandparent, Grandchild) :- parent(Grandparent, Parent), parent(Parent, Grandchild).
sibling(Sibling1, Sibling2) :- parent(Parent, Sibling1), parent(Parent, Sibling2), Sibling1 \= Sibling2.
% Additional facts for gender
male(john).
male(jim).
male(tom).
female(susan).
female(ann).
female(emily).
% Queries
?- father(john, jim). % true
?- mother(susan, jim). % true
?- grandparent(john, emily). % true
?- sibling(jim, ann). % false
```
_____________________________________________________________________________________________________________________________

In this Prolog example:
1. **Facts:** `parent/2` represents parent-child relationships.
2. **Rules:** We have rules for `father/2`, `mother/2`, `grandparent/2`, and `sibling/2`. These rules define
relationships based on parent-child connections and gender.
3. **Additional facts for gender:** `male/1` and `female/1` define the gender of individuals.
4. **Queries:** The queries demonstrate how to ask about relationships in the family tree.
- `?- father(john, jim).`: Asks if John is the father of Jim. Prolog responds with `true`.
- `?- mother(susan, jim).`: Asks if Susan is the mother of Jim. Prolog responds with `true`.
- `?- grandparent(john, emily).`: Asks if John is the grandparent of Emily. Prolog responds with `true`.
- `?- sibling(jim, ann).`: Asks if Jim and Ann are siblings. Prolog responds with `false`.
You can expand and modify this example to create a more detailed family tree with additional relationships
and facts.

_______________________________________________________________________________________________________________________________