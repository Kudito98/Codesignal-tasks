def solution(number):
    letterList = []
    secondLetter = ord(number)-65
    firstLetter = 0
    while  firstLetter < secondLetter + 1:
        numSum = str(chr(firstLetter + 65)) + " + "+ str(chr(secondLetter + 65))
        letterList.append(numSum)
        firstLetter += 1
        secondLetter -= 1
        
    return letterList