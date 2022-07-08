def solution(n):
    stnum = str(n)
    res = 0
    for i in range(len(stnum)-1):
        if int(stnum[i]) < int(stnum[i+1]):
            res = int(stnum[:i] + stnum[i+1:])
            break
    if res == 0:
        res = int(stnum[:-1])
    return res
