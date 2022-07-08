def solution(inputArray):
    iA = inputArray
    c = 0
    for i in range(len(iA) - 1):
        if iA[i] >= iA[i + 1]:
            d = iA[i] - iA[i + 1]
            iA[i + 1] += d + 1
            c += d + 1
    return c

