def solution(n):
    return [[0]*min(x, 2*n-x) for x in range (1,2*n)]
