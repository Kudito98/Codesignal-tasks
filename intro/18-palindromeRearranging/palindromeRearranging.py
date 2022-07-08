def solution(inputString):
    temp = list()
    odd_cnt = 0
    if len(set(inputString)) == 1:
        return True
    for i in set(inputString):
        print(inputString.count(i))
        if inputString.count(i) % 2 == 1:
            odd_cnt += 1
        else:
            continue
    if odd_cnt <= 1:
        return True
    else:
        return False