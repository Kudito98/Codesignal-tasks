def solution(l, r):
    c = 0

    def s(number):
        sum_digit = sum(int(digit) for digit in str(number))
        return sum_digit
        
    for a in range(l, r):
        for b in range(a + 1, r + 1):
            if (a - s(a)) <= b <= (a + s(a)) and (b - s(b) <= a <= b + s(b)):
                c += 1
    return c
