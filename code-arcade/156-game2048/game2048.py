def solution(grid, path):
    for m in path:
        grid = transform(grid, m, False)
        grid = list(map(merge, grid))
        grid = transform(grid, m, True)
    return list(grid)

def transform(grid, move, inv):
    if move == "L":
        return grid
    elif move == "R":
        return [l[::-1] for l in grid]
    elif move == "U":
        return list(zip(*grid))
    elif move == "D" and not inv:
        return list(zip(*(grid[::-1])))
    elif move == "D":
        return list(zip(*grid))[::-1]
    else:
        return grid

def merge(line):
    i = 0
    newLine = [0]*4
    
    for n in line:
        if n == 0:
            continue
        if newLine[i] == 0:
            newLine[i] = n
        elif newLine[i] == n:
            newLine[i] += n
            i += 1 
        else:
            i += 1
            newLine[i] = n
        
    return newLine
