def solution(male, female):
    return [[x for x, y in zip(male, female) if x != y], [y for x, y in zip(male, female) if y != x]]
