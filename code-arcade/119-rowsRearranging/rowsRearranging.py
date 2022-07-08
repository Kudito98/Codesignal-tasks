def solution(matrix):
    matrix = sorted(matrix, key = lambda m: m[0])
    for i in range(len(matrix[0])):
        for j in range(len(matrix)-1):
            if matrix[j+1][i]<=matrix[j][i]:
                return False
    return True
