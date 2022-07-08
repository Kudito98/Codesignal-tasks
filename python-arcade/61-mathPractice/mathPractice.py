def solution(numbers):
    return functools.reduce(lambda a, b: (a + b[1] if b[0]%2 else a*b[1]), enumerate(numbers), 1)
