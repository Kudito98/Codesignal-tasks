def solution(items):
    newItems = []
    for i in range(len(items)):
        pos = -1
        for j in range(i):
            if items[j] < items[i]:
                pos = j
        if pos == -1:
            newItems.append(-1)
        else:
            newItems.append(items[pos])
    return newItems
            
