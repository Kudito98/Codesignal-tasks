def solution(matrix):
    res_set = set()
    temp_str = ""
    
    for i in range(len(matrix)- 1):
        for j in range(len(matrix[0]) - 1):
            temp_str = str(matrix[i][j]) + str(matrix[i + 1][j]) + str(matrix[i][j + 1]) + str(matrix[i + 1][j + 1])
            res_set.add(temp_str)
            
    return len(res_set)
