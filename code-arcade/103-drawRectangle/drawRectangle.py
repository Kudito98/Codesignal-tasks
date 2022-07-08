def solution(canvas, rectangle):
    x1 = rectangle[0]
    y1 = rectangle[1]
    x2 = rectangle[2]
    y2 = rectangle[3]
    
    canvas[y1][x1] = '*'
    canvas[y1][x2] = '*'
    canvas[y2][x1] = '*'
    canvas[y2][x2] = '*'
    for i in range(x1+1,x2):
        canvas[y1][i] = '-'
        canvas[y2][i] = '-'
    for i in range(y1+1,y2):
        canvas[i][x1] = '|'
        canvas[i][x2] = '|'
    
    return canvas
