def solution(shuffled):
    for i, e in enumerate(shuffled):
        left = shuffled[:i]
        right = shuffled[i+1:]
        if sum(left)+sum(right) == e:
            return sorted(left + right)
