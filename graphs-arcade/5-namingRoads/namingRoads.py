from collections import defaultdict

def solution(roads):
    cities = defaultdict(set)
    for c1, c2, r in roads:
        cities[c1].add(r)
        cities[c2].add(r)
    
    for s in cities.values():
        for v in s:
            if v-1 in s or v+1 in s:
                return False
    
    return True