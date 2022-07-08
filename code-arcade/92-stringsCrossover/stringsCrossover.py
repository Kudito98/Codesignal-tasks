def solution(inputArray, result):
    t = 0
    for i in range(len(inputArray)):
        for j in range( i + 1, len(inputArray)):
            for k in range(len(result)):
                if not (inputArray[i][k] == result[k] or inputArray[j][k] == result[k]):
                    break
            else:
                t += 1
    return t
