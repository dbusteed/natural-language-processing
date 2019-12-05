% PROLOG fun with family relationships. see relationships.png
% for a diagram that shows the relationships of the dummy data

% SOME DEFINITIONS

male(charlie).
male(steve).
male(raymond).
male(frank).
male(bobby).
male(jake).
male(ernie).
male(peter).
male(andrew).

female(june).
female(sally).
female(susan).
female(jan).
female(april).
female(doris).
female(paula).
female(erica).
female(lucy).

parent(ernie,susan).
parent(ernie,paula).
parent(doris,susan).
parent(doris,paula).

parent(raymond,charlie).
parent(raymond,sally).
parent(raymond,steve).
parent(susan,charlie).
parent(susan,sally).
parent(susan,steve).

parent(paula,andrew).
parent(peter,andrew).

parent(steve,bobby).
parent(steve,april).
parent(jan,bobby).
parent(jan,april).

parent(sally,jake).
parent(frank,jake).

parent(andrew,lucy).
parent(erica,lucy).

spouse(ernie,doris).
spouse(doris,ernie).

spouse(raymond,susan).
spouse(susan,raymond).
spouse(peter,paula).
spouse(paula,peter).

spouse(charlie,june).
spouse(june,charlie).
spouse(sally,frank).
spouse(frank,sally).
spouse(steve,jan).
spouse(jan,steve).
spouse(andrew,erica).

sibling(paula,susan).
sibling(susan,paula).

sibling(charlie,sally).
sibling(charlie,steve).
sibling(sally,steve).
sibling(sally,charlie).
sibling(steve,charlie).
sibling(steve,sally).

sibling(bobby,april).
sibling(april,bobby).


% RULES

% (X,Y) means "X is the BLANK of Y", or "X is Y's blank"

husband(X,Y) :- male(X) , spouse(X,Y).
wife(X,Y) :- female(X) , spouse(X,Y).

child(X,Y) :- parent(Y,X).

brother(X,Y) :- male(X) , sibling(X,Y).
sister(X,Y) :- female(X) , sibling(X,Y).

grandParent(X,Y) :- parent(X,Z) , parent(Z,Y).
grandFather(X,Y) :- grandParent(X,Y) , male(X). 
grandMother(X,Y) :- grandParent(X,Y) , female(X).
grandChild(X,Y) :- grandParent(Y,X).
grandSon(X,Y) :- male(X) , grandChild(X,Y).
grandDaughter(X,Y) :- female(X) , grandChild(X,Y).

greatGrandParent(X,Y) :- parent(X,Z) , grandParent(Z,Y).
greatGrandFather(X,Y) :- male(X) , greatGrandParent(X,Y).
greatGrandMother(X,Y) :- female(X) , greatGrandParent(X,Y).
greatGrandChild(X,Y) :- greatGrandParent(Y,X).
greatGrandSon(X,Y) :- male(X) , greatGrandChild(X,Y).
greatGrandDaugter(X,Y) :- female(X) , greatGrandChild(X,Y).

uncle(X,Y) :- parent(Z,Y) , male(X) , ( sibling(Z,X) ; ( sibling(Q,Z) , spouse(X,Q) ) ).
aunt(X,Y) :- parent(Z,Y) , female(X) , ( sibling(Z,X) ; ( sibling(Q,Z) , spouse(X,Q) ) ).
nephew(X,Y) :- uncle(Y,X).
niece(X,Y) :- aunt(Y,X).

cousin(X,Y) :- parent(Q,X) , parent(Z,Y) , sibling(Q,Z).
cousinInLaw(X,Y) :- cousin(X,Z) , spouse(Z,Y).

inLaw(X,Y) :- parent(X,Z) , spouse(Z,Y).
fatherInLaw(X,Y) :- male(X) , inLaw(X,Y).
motherInLaw(X,Y) :- female(X) , inLaw(X,Y).

siblingInLaw(X,Y) :- ( spouse(X,Z) , sibling(Z,Y) ) ; ( spouse(X,Z) , ( sibling(Z,Q) ; sibling(X,Q) ) , spouse(Q,Y) ).
sisterInLaw(X,Y) :- siblingInLaw(X,Y) , female(X).
brotherInLaw(X,Y) :- siblingInLaw(X,Y) , male(X).

grandAunt(X,Y) :- aunt(X,Z) , parent(Z,Y).
grandUncle(X,Y) :- uncle(X,Z) , parent(Z,Y).
grandNephew(X,Y) :- male(X) , ( grandAunt(Y,X) ; grandUncle(Y,X) ).
grandNiece(X,Y) :- female(X) , ( grandAunt(Y,X) ; grandUncle(Y,X) ).

secondCousin(X,Y) :- ( grandAunt(Z,X) ; grandUncle(Z,X) ) , grandChild(Y,Z).