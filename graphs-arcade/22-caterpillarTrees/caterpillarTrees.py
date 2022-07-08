from collections import defaultdict

def solution(n, edges):
    adj = defaultdict(set)
    for i,j in edges:
        adj[i].add(j)
        adj[j].add(i)
        
    def check(k, prev=None, root=True):
        if k not in adj:
            return False, False, 0

        others = [i for i in adj.pop(k) if i != prev]
        if not others:
            return True, True, 0
        
        outer = len(others) is 1
        tree, cat, mid = zip(*(check(i, k, root and outer) for i in others))
        return all(tree), all(cat) and sum(mid) <= (1+root), 1

    count = [n - len(adj)] * 2
    while adj:
        k = next(iter(adj))
        tree, cat, _ = check(k)
        count[0] += tree
        count[1] += cat
    return count
