def solution(inputArray):
    jump = 1
    while len(inputArray) > 1:
        currentArray = []
        if jump % 2 == 0:
            for i in range(0, len(inputArray)-1, 2):
                a = inputArray[i] * inputArray[i+1]
                currentArray.append(a)
        else:
            for i in range(0, len(inputArray)-1, 2):
                a = inputArray[i] + inputArray[i+1]
                currentArray.append(a)
        
        inputArray = currentArray
        jump += 1
    return inputArray[0]