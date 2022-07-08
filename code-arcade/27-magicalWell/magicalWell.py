def solution(a, b, n):
    money = 0
    while n != 0:
        money = money + (a * b)
        n -= 1
        a += 1
        b += 1
    return money