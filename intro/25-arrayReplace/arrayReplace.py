def solution(inputArray, elemToReplace, substitutionElem):
    newArray = []
    for i in inputArray:
        if i == elemToReplace:
            newArray.append(substitutionElem)
        else:
            newArray.append(i)
    return newArray