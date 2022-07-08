from itertools import combinations

def solution(players, k):
    return sorted(list(combinations(sorted(players), k)))
