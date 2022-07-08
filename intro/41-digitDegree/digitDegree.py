def solution(n):
    count = 0
    while len(str(n)) != 1:
        count += 1
        sum_digit = 0
        for digit in str(n):
            sum_digit += int(digit)
            n = sum_digit
    return count

