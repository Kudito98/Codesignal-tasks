def solution(n):
    count = 0
    l = 1
    while(l * (l + 1) < 2 * n):
        a = (n - (l * (l + 1) ) / 2) / (l + 1)
        if (a - int(a) == 0):
            count += 1
        l += 1
    return count
