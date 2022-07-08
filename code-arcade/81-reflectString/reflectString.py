def solution(inputString):
    newWord = ""
    for i in inputString:
        newWord += chr(122-(ord(i)-97))
        
    return newWord
