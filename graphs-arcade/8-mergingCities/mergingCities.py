def solution(roadRegister):
    newRegister = roadRegister
    c, n = 0, len(newRegister)
    
    while c < n-1:
        if newRegister[c][c+1] and newRegister[c+1][c]:
            r = range(n)
            for k in r:
                newRegister[c][k] |= newRegister[c+1][k] and c!=k
                newRegister[k][c] |= newRegister[k][c+1] and c!=k

            newRegister = [[newRegister[i][j] for j in r if j!=c+1] for i in r if i!=c+1]
            n -= 1
            c += 1

        else:
            c += 2
    
    return newRegister