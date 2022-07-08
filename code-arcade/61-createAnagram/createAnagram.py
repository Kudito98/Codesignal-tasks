from collections import Counter
def solution(s, t):
    tc = Counter(t)
    sc = Counter(s)
    res = 0
    for c in tc:
        d = tc[c] - sc[c]
        if d < 0:
            d = 0
        res += d
    return res