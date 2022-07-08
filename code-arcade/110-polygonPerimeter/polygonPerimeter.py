def solution(matrix):
    nrow = len(matrix)
    ncol = len(matrix[0])
    perimeter = 0
    for i in range(nrow):
        for j in range(ncol):
            if matrix[i][j]:
                perimeter += 4
    
    for i in range(nrow):
        for j in range(ncol):
            if j != ncol-1:
                if matrix[i][j] and matrix[i][j+1]:
                    perimeter -= 2
            if i != nrow-1:
                if matrix[i][j] and matrix[i+1][j]:
                    perimeter -= 2
    
    return perimeter