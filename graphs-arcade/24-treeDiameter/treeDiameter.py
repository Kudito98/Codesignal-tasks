from collections import defaultdict

def solution(n, tree):
    g = defaultdict(set)
    
    for a, b in tree:
        g[a].add(b)
        g[b].add(a)

    def t(b):
        m = b, 0
        v, q = {b}, [m]
        
        while q:
            n, c = q.pop()
            
            if m[1] < c:
                m = n, c
                
            s = g[n] - v
            q += [(i, c + 1) for i in s]
            v |= s
            
        return m
    
    return t(t(0)[0])[1]