def solution(morning, evening):
    return [list(map(lambda x, y: x if x <=y else y, morning, evening)) , list(map(lambda x, y: x if x >= y else y, morning, evening))]