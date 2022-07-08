def solution(shoes):
    leftshoe = []
    rightshoe = []
    for i in range(len(shoes)):
        if (shoes[i])[0] == 0:
            leftshoe.append(shoes[i])
        else:
            rightshoe.append(shoes[i])
    rs = sorted(rightshoe)
    ls = sorted(leftshoe)
    if len(rs) == len(ls):
        for i in range(int(len(shoes)/2)):
            if (rs[i])[1] == (ls[i])[1]:
                continue
            else:
                return False
    else:
        return False
    
    return True