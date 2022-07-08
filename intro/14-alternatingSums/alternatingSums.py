def solution(a):
    la = [a[i] for i in range(len(a)) if i % 2 == 0]
    lb = [a[i] for i in range(len(a)) if i % 2 != 0]
    sum1 = sum(la)
    sum2 = sum(lb)
    return [sum1, sum2]