def solution(adj):
    checkList = [2, 2, 2, 2, 4]
    diag = []
    createList = []
    for i in range(len(adj)):
        a = sum(adj[i])
        d = adj[i][i]
        createList.append(a)
        diag.append(d)
    return checkList == sorted(createList) and sum(diag) == 0
