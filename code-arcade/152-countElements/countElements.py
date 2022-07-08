def solution(inputString):
    iS = inputString.replace("t", "T").replace("f", "F")
    print(eval(iS))
    return count(eval(iS))

def count(x):
    if type(x) != list:
        return 1
    else:
        return sum(map(count, x))