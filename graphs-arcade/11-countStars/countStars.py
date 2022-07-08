def solution(adj):
    numConnections = [sum(row) for row in adj]
    numStars = 0
    for i in range(len(adj)):
        if numConnections[i] == 0:
            continue
        for j in range(len(adj)):
            if adj[i][j]:
                if numConnections[j] > 1:
                    break
                if numConnections[i] == 1 and j <= i:
                    break
        else:
            numStars += 1
    return numStars
