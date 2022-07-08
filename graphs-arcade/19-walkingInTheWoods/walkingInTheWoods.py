from collections import defaultdict

def solution(n, wmap):
    adj = defaultdict(list)
    for i, j in wmap:
        adj[i].append(j)
        adj[j].append(i)
    
    def explore(node):
        for dest in adj.pop(node, []):
            explore(dest)
    
    graphs = n - len(adj)
    while adj:
        explore(next(iter(adj)))
        graphs += 1
    return graphs - 1