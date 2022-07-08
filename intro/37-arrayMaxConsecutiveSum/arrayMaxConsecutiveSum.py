def solution(inputArray, k):
    res = 0
    for i in range(k):
        res += inputArray[i]
 
    curr_sum = res
    for i in range(k, len(inputArray)):
        curr_sum += inputArray[i] - inputArray[i-k]
        res = max(res, curr_sum)
 
    return res