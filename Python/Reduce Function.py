from fractions import Fraction
from functools import reduce
import operator
def product(fracs):
    t = reduce(operator.mul,fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
