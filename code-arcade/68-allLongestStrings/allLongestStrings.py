def solution(inputArray):
    lenMaxWords = len(sorted(inputArray, key=lambda el: -len(el))[0])
    wordList = []
    for i in inputArray:
        if len(i) == lenMaxWords:
            wordList.append(i)
    return wordList