def solution(arr):
    if len(arr) % 2 == 0:
        index = int(len(arr) / 2)
        middle_sum = arr[index-1] + arr[-index]
        res = []
        res.extend(arr[:index - 1])
        res.append(middle_sum)
        res.extend(arr[index+1::])
        return res
    else:
        return arr
