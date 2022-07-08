def solution(cities, roads):
    res = []
    for i in range(0,cities):
        for j in range(i+1, cities):
            if [i,j] not in roads and [j,i] not in roads:
                    res.append([i,j])
    return res