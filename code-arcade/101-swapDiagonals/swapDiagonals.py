def solution(matrix):
    mL = len(matrix)-1
    for i in range(int(mL/2)+1):
        for j in range(mL):
            if i == j:
                #first diagonal
                matrix[i][j], matrix[i][mL-j] = matrix[i][mL-j], matrix[i][j]
                #second diagonal
                matrix[mL-i][j], matrix[mL-i][mL-j] = matrix[mL-i][mL-j], matrix[mL-i][j]
    return matrix
