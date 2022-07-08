def solution(a, b):
    swaperror = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        elif swaperror <= 1:
            swaperror += 1
            continue
        else:
            return False
            
    la = sorted(a)
    lb = sorted(b)
    boolist = []
    for i in range(len(a)):
        if la[i] == lb[i]:
            boolist.append(1)
        else:
            boolist.append(0)
    return False if boolist.count(0) else True
