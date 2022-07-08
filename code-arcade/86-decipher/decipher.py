def solution(cipher):
    uncodedString = ""
    letterCode = ""
    for i in cipher:
        letterCode += i
        if int(letterCode) - 97 >= 0:
            uncodedString += chr(int(letterCode))
            letterCode = ""
    return uncodedString
