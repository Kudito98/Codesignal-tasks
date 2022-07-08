def solution(inputArray, elemToReplace, substitutionElem):
    nlst = []
    for i in inputArray:
        if i == elemToReplace:
            nlst.append(substitutionElem)
        else:
            nlst.append(i)
    return nlst
