def solution(arr):
    if len(arr) <= 1:
        return arr
    elif len(arr) == 2:
        return [arr[1], arr[0]]
    else:
        nlst = []
        nlst.append(arr[-1])
        for i in range(1, len(arr)-1):
            j = arr[i]
            nlst.append(j)
        nlst.append(arr[0])
        return nlst