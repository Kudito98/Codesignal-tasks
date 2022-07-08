def solution(n, m):
    candi = 0
    while True:
        if candi <= m:
            candi += n
        else:
            return candi - n 
