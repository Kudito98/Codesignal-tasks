def solution(a):
    return functools.reduce(lambda l, x: l + [l[-1] + x], a,[0])[1:]
