def solution(a, b):
    return sum([x for x in range(max(a,2), b+1) if not 0 in [x%z for z in range(2, int(x**.5+1))]])


