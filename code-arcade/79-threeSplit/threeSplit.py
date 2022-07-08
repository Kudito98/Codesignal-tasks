def solution(a):
    tot = sum(a) // 3
    ans = 0
    cur = 0
    first = 0 
    
    for i in range(len(a) - 1):
        cur += a[i]
        if cur == tot:
            first += 1
        if cur == 2 * tot:
            ans += first
            if tot == 0:
                ans -= 1
                
    return ans
