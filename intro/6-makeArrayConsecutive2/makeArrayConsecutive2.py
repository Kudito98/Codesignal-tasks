def solution(statues):
    return len(set(range(min(statues), max(statues)+1))-set(statues))
