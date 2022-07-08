def solution(inputString):
    numbers = ""
    for i in inputString:
        if i.isdigit():
            numbers += i
        else:
            numbers += " "
    digits = numbers.split(" ")
    total = 0
    for i in digits:
        if i.isdigit():
            total += int(i)
        else:
            continue
    return total