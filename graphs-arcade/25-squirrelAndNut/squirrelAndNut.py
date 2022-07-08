def branch(parents, u):
    p = [u]

    while parents[u]:
        u = parents[u]
        p.append(u)

    return p

def inPath(parents, a, b, c):
    # print(a, b, c)
    
    pa = branch(parents, a)
    pb = branch(parents, b)
    
    # print(a, pa)
    # print(b, pb)
    
    while len(pa) > 1 and len(pb) > 1 and pa[-2] == pb[-2]:
        pa.pop()
        pb.pop()
    
    return c in set(pa + pb)

def solution(tree, triples):
    n = len(tree) // 2
    parents = [0] * (n + 2)
    
    for u, v in ((tree[2 * i], tree[2 * i + 1]) for i in range(n)):
        parents[v] = u

    # print(parents)

    return [inPath(parents, a, b, c) for a, b, c in triples]