def solution(matrix):
    squares = []
    for l in range(len(matrix)-1):
        for k in range(len(matrix[0])-1):
            a = (matrix[l][k], matrix[l][k+1], matrix[l+1][k], matrix[l+1][k+1])
            if a not in squares:
                squares.extend([a])
    return len(squares)
   