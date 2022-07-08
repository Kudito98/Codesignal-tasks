from math import gcd

def solution(denominators):
    return functools.reduce(lambda x, y: abs(x*y)//math.gcd(x, y), denominators)
