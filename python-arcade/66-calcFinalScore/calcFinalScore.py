def solution(scores, n):
    gen = (i**2 for i in sorted(scores, reverse = True))

    res = 0
    try:
        for _ in range(n):
            res += next(gen)
    except StopIteration:
        res //= 5

    return res
