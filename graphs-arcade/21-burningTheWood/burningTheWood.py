from collections import defaultdict

def solution(n, wmap, start, k):
    adj = defaultdict(set)
    for s, e in wmap:
        adj[s].add(e)
        adj[e].add(s)
        
    burning = {start}
    while k:
        new = set()
        for m in burning:
            new |= adj[m]
        burning |= new
        k -= 1
    
    return sorted(burning)
    