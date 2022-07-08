def solution(a):
    trees = [i for i, x in enumerate(a) if x == -1]
    res = sorted(a)[len(trees):]
    
    for i in trees:
        res.insert(i, -1)
        
    return res
