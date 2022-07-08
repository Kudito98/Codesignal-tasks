def solution(inputString):
    if '-' not in inputString:
        return False
    splitData = inputString.split('-')
    if len(splitData) != 6:
        return False
    for data in splitData:
        if len(data) != 2:
            return False
        if not ((ord('0') <= ord(data[0]) <= ord('9')) or (ord('A') <= ord(data[0]) <= ord('F'))):
            return False
        if not ((ord('0') <= ord(data[1]) <= ord('9')) or (ord('A') <= ord(data[1]) <= ord('F'))):
            return False
        else:
            continue
    return True