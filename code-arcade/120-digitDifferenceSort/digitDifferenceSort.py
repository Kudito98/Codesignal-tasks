def solution(a):
    diff = [list(str(i)) for i in a]
    for i in range(len(diff)):
        diff[i] = [int(j) for j in diff[i]]
        diff[i] = max(diff[i])-min(diff[i])
    indices = [i for i in range(len(a))]
    combined = [list(i) for i in zip(diff,a,indices)]
    combined = sorted(combined,key = lambda x: (x[0],-x[2]))
    a = [x[1] for x in combined]
    return a
