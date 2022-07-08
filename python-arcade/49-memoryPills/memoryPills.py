from itertools import dropwhile

def solution(pills):
    gen = dropwhile(lambda x: len(x) % 2, pills + ["", "", ""])
    next(gen)
    return [next(gen) for _ in range(3)]
