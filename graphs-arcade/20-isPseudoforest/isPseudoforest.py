from collections import defaultdict

def solution(n, wmap):
    adj = defaultdict(set)
    for s, e in wmap:
        adj[s].add(e)
        adj[e].add(s)
    
    def explore(node):
        if node not in adj:
            return 1
        count = -1
        for dest in adj.pop(node, []):
            count += explore(dest)
        return count
    
    while adj:
        if explore(next(iter(adj))) > 1:
            return False
    return True
    