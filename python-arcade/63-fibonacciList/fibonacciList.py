def solution(n):
    return [[0] * x for x in functools.reduce(lambda x, y: x+[x[-1] + x[-2]], range(n-2), [0, 1])]
