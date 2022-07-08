def solution(boardSize, initPosition, initDirection, k):
    m = boardSize[0]
    n = boardSize[1]
    if (m == 1 and n == 1):
        return [0, 0]
    
    x = initPosition[0]
    y = initPosition[1]
    dx = initDirection[0]
    dy = initDirection[1]
    cache = [x, y, dx, dy]
    while (k > 0):
        k -= 1
        x1 = x + dx
        y1 = y + dy
        if (x1 < 0 or x1 >= m):
            x1 = x
            dx = -dx

        if (y1 < 0 or y1 >= n):
            y1 = y
            dy = -dy
        
        x = x1
        y = y1
        state = [x, y, dx, dy]
        
        for i in range(len(cache)):
            if (cache[i] == state):
                c = len(cache) - i
                r = (k + 1) % c
                final_state = cache[i + (r + c - 1) % c]
                return [final_state[0], final_state[1]]
        
        cache.append(state)
    return [x, y]