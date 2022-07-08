def solution(matrix, a, b):
    row = len(matrix)
    col = len(matrix[0])
    Sum = 0
    for i in range(0,row):
        Sum += matrix[i][b]
    for j in range(0,col):
        Sum += matrix[a][j]
    return Sum-matrix[a][b]
