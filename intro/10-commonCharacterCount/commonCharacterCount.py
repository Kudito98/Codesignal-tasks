from collections import Counter

def solution(s1, s2):
    cs1 = Counter(s1)
    cs2 = Counter(s2)
    if len(cs1) > len(cs2):
        ncs1 = cs1 - (cs1 - cs2)
        return sum(ncs1.values())
    else:
        ncs2 = cs2 - (cs2 - cs1)
        return sum(ncs2.values())
    
        
        

