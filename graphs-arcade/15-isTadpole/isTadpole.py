def solution(adj):
    return solutionSignature(adj) and isConnected(adj)


def solutionSignature(adj):
    return sorted(sum(row) for row in adj) == [1] + [2] * (len(adj) - 2) + [3]


def isConnected(adj):
    removeConnectedTrues(adj, 0)
    return not any(any(row) for row in adj)


def removeConnectedTrues(adj, j):
    for i in range(len(adj)):
        if adj[i][j]:
            adj[i][j] = adj[j][i] = False
            removeConnectedTrues(adj, i)