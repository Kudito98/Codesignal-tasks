def solution(matrix, width, center, t):
    rowCenter = center[0]
    colCenter = center[1]
    width //= 2
    for j in range(t%360):
        for i in range(width):
            temp = matrix[rowCenter-width+i][colCenter-width+i]
            matrix[rowCenter-width+i][colCenter-width+i] = matrix[rowCenter][colCenter-width+i]
            matrix[rowCenter][colCenter-width+i] = matrix[rowCenter+width-i][colCenter-width+i]
            matrix[rowCenter+width-i][colCenter-width+i] = matrix[rowCenter+width-i][colCenter]
            matrix[rowCenter+width-i][colCenter] = matrix[rowCenter+width-i][colCenter+width-i]
            matrix[rowCenter+width-i][colCenter+width-i] = matrix[rowCenter][colCenter+width-i]
            matrix[rowCenter][colCenter+width-i] = matrix[rowCenter-width+i][colCenter+width-i]
            matrix[rowCenter-width+i][colCenter+width-i] = matrix[rowCenter-width+i][colCenter]
            matrix[rowCenter-width+i][colCenter] = temp
    return matrix