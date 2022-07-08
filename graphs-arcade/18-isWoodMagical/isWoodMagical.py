from collections import defaultdict

def solution(n, wmap):
    adj_list = defaultdict(set)
    for s, e in wmap:
        if s == e:
            return False
        adj_list[s].add(e)
        adj_list[e].add(s)
        
    colors = [0]*n
    for i in range(n):
        for j in adj_list[i]:
            if colors[j] == 0:
                colors[j] = colors[i] + 1
            elif colors[j] == colors[i]:
                return False
    
    return True
    