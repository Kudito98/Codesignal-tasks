def solution(adj):
    return not isSelfConnecting(adj) and solutionSignature(adj)

def isSelfConnecting(adj):
    return any(adj[i][i] for i in range(len(adj)))
    
def solutionSignature(adj):
    return sorted(sum(row) for row in adj) == [2] * (len(adj) - 2) + [len(adj) - 1] * 2
    
    