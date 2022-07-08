from collections import defaultdict
def solution(n, roads):
    vertices = defaultdict(set)
    
    for road in roads:
        x, y = road
        vertices[x].add(y)
        vertices[y].add(x)
    
    for i in range(n):
        for j in range(i + 1, n):
            if i in vertices[j] or len(vertices[i] & vertices[j]) >= 1:
                continue
            else:
                return False
    print(vertices)
    return True
