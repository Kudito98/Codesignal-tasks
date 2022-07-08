from collections import defaultdict
from queue import LifoQueue

def solution(n, roads):        
    res = [-1]*n
    survivors = defaultdict()
    for c in range(n):
        survivors[c] = set()

    for a, b in roads:
        survivors[a].add(b)
        survivors[b].add(a)

    day = 1
    isChange = True
    toRemove = LifoQueue(n)
    while isChange:
        for c in survivors.keys():
            if len(survivors[c] & set(survivors.keys())) <= 1:
                res[c] = day
                toRemove.put(c)

        isChange = not toRemove.empty()
        while not toRemove.empty():
            survivors.pop(toRemove.get())
            
        day += 1
    
    return res
