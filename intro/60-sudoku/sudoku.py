def ValidRow(grid, row):
    check_list = []
    for i in range(len(grid)):
        if grid[row][i] in check_list:
            return False
        else:
            check_list.append(grid[row][i])
    return True
    
def ValidCol(grid, col):
    check_list = []
    for i in range(len(grid)):
        if grid[i][col] in check_list:
            return False
        else:
            check_list.append(grid[i][col])
    return True

def ValidBox(grid, startRow, startCol):
    check_list = []
    for row in range(3):
        for col in range(3):
            box_val = grid[startRow + row][startCol + col]
            if box_val in check_list:
                return False
            else:
                check_list.append(box_val)
    return True

def solution(grid):
    #check validation for each row
    for row in range(len(grid)):
        if ValidRow(grid, row) == False:
            return False
    #check validation for each column
    for col in range(len(grid)):
        if ValidCol(grid, col) == False:
            return False
    #check validation for 3x3 each box
    for row in range(0, len(grid), 3):
        for col in range(0, len(grid), 3):
            if ValidBox(grid, row, col) == False:
                return False
    return True
        

