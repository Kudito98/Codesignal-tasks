def solution(matrix):
    total = 0
    for column in zip(*matrix):
        for cost in column:
            if cost == 0:
                break
            total += cost

    return total
