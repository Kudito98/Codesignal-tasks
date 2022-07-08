def solution(adj):
    n = len(adj)
    x = (n/2)-1
    arr = []
    for i in range(n):
        c3 = adj[i].count(True)
        if x != c3:
            return False
            
        if adj[i][i] == True:
            return False
            
        if adj[0][i] == True:
            arr.append(i)
    
    if c3 == 0:
        return False

    for i in range(n):
        if adj[arr[0]][arr[1]] == True:
            return False
    
    return True