def solution(statues):
    return len([i for i in range(min(statues), max(statues) +1)]) - len(statues)
        
    