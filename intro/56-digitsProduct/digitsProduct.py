def solution(product):
    for i in range (1, 10000):
        number = str(i)
        total = 1
        for char in number:
            total *= int(char)
            if total == product:
                return i
    #if not found return -1
    return -1