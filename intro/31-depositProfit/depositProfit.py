def solution(deposit, rate, threshold):
    year = 0
    while deposit < threshold:
        uppcash = 1 + (rate/100)
        deposit = deposit * uppcash
        year += 1
    return year
