def solution(a):
    length = len(a)
    a = sorted(set(a))
    numGroup = 0
    
    while a:
        bound = (a[0]-1)//pow(10,4)+1
        numGroup += 1
        while a and a[0]<=bound*pow(10,4):
            a.pop(0)
    
    return numGroup+length