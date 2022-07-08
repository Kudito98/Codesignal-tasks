def solution(n, l, r):
    return max(0, round(min(n/2-l, r-n/2) + (n+1)%2))

