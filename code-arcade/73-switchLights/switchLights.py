def solution(a):
    for i in range(len(a)):
        if a[i] == 1:
            for j in range(i+1):
                a[j] = int(not a[j])     
    return a
    