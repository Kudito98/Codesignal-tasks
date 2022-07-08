from collections import defaultdict, Counter

def solution(n, ladder):
    adj = defaultdict(set)
    for e, s in ladder:
        adj[e].add(s)
        adj[s].add(e)
        
    if {3: n} != Counter(map(len, adj.values())):
        return False
    
    def check(px, py, x):
        goal = (py, px)
        y = next((z for z in adj[py] if z!=px and x in adj[z]), None)
        if y is None:
            return False

        for _ in range(n//2 - 1):
            try:
                nx = next(z for z in adj[x] if z not in (y, px))
                ny = next(z for z in adj[y] if z not in (x, py))
            except:
                return False
            x, y, px, py = nx, ny, x, y
        return (x, y) == goal
    
    a, b, c = list(adj[0])
    return check(0,a,b) or check(0,b,a) or check(0,c,a)