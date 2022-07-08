def solution(inputString):
    halfLenString = int(len(inputString)/2)
    
    word1 = inputString[0:halfLenString]
    word2 = inputString[halfLenString:]
    
    if word1 == word2:
        return True
    else:
        return False
    