def solution(n):
    if n == 1:
        return 1
    else:
        return solution(n-1)+4*n-4

