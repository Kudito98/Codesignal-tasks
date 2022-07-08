def solution(inputArray):
    res = 0
    mylist = []
    for i in range(len(inputArray)-1):
         res = abs(inputArray[i+1] - inputArray[i])
         mylist.append(res)
    return max(mylist)
