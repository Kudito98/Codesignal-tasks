def solution(matrix, column):
    res = []
    for row in matrix:
        for j, k in enumerate(row):
            if j == column:
                res.append(k)
    return res
