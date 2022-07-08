def solution(n):
    s = [int(x) for x in str(n)]
    l = int(len(s)/2)    
    return sum(s[:l]) == sum(s[l:])
    

