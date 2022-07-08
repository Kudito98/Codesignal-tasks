def solution(table, coords):
    table = list(map(list, table))
    rdivs = [i for i, row in enumerate(table) if row[0] == "+"]
    cdivs = [i for i, col in enumerate(table[0]) if col == "+"]
    
    x1, y1 = rdivs[coords[1][0]], cdivs[coords[0][1]]
    x2, y2 = rdivs[coords[0][0] + 1], cdivs[coords[1][1] + 1]
    
    for x in range(x1 + 1, x2):
        if y1 == 0:
            table[x][y1] = "|"
        if y2 == len(table[0]) - 1:
            table[x][y2] = "|"
            
        for y in range(y1 + 1, y2):
            if table[x][y] in "|-+":
                table[x][y] = " "
    
    for y in range(y1 + 1, y2):
        if x1 == 0:
            table[x1][y] = "-"
        if x2 == len(table) - 1:
            table[x2][y] = "-"
    return list(map(lambda x: "".join(x), table))
