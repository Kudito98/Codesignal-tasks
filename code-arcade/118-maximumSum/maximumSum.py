def solution(a, q):
    a.sort()
    b = [0]*len(a)
    
    for e in q:
        for i in range(e[0],e[1]+1):
            b[i] += 1
            
    b.sort()
    res = 0
    
    for i in range(len(a)):
        res += a[i]*b[i]
    return res
