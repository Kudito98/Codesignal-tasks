def solution(a):
    sum = 0
    for i in range(len(a)):
        sum += a[len(a) - i - 1] * int(math.pow(256, (len(a) - i - 1)))
    return sum