def solution(adj):
    petalRank, solutionSignature = flowerSignature(adj)
    return solutionSignature and not isSelfConnecting(adj) and getNPetals(adj) * petalRank == len(adj) - 1
    

def isSelfConnecting(adj):
    return any(adj[i][i] for i in range(len(adj)))

def flowerSignature(adj):
    counts = sorted(sum(row) for row in adj)
    petalRank = counts[0]
    return petalRank,  petalRank >= 2 and counts[-1] == len(adj) - 1 and all(petalRank == c for c in counts[:-1])

def getNPetals(adj):
    removeCenter(adj)
    n = 0
    for i, row in enumerate(adj):
        if any(row):
            n += 1
            removeConnectedTrues(adj, i)
    return n
    
def removeCenter(adj):
    center = max(range(len(adj)), key=lambda i: sum(adj[i]))
    for i in range(len(adj)):
        adj[center][i] = adj[i][center] = False
    
def removeConnectedTrues(adj, j):
    for i in range(len(adj)):
        if adj[i][j]:
            adj[i][j] = adj[j][i] = False
            removeConnectedTrues(adj, i)