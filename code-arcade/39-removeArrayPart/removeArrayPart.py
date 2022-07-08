def solution(inputArray, l, r):
    B = []
    for i in range(len(inputArray)):
        if (i < l or i > r):
            B.append(inputArray[i])
    return B