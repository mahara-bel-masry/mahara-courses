import itertools
from fractions import Fraction
space = list(itertools.product(range(1, 7), repeat=2))
print("outcomes for two dice", len(space))
even = [o for o in space if sum(o) % 2 == 0]
print("sum even", len(even), Fraction(len(even), len(space)))
seven = [o for o in space if sum(o) == 7]
print("sum seven", len(seven), Fraction(len(seven), len(space)))
double = [o for o in space if o[0] == o[1]]
print("double", len(double), Fraction(len(double), len(space)))
print("seven or double", len([o for o in space if sum(o) == 7 or o[0] == o[1]]))
