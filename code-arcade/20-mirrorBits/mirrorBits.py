def solution(a):
    b = bin(a)[2::][::-1]
    x = 0
    x = int(b, base = 2)
    return int(x)