def solution(n):
    number = str(n)
    for i in number:
        if int(i) % 2 == 0:
           continue
        else:
            return False
    return True