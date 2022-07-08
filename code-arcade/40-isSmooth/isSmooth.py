def solution(arr):
    if arr[0] == arr[-1]:
        if len(arr) % 2 == 0:
            index = int(len(arr) / 2)
            middle_sum = int(arr[index-1] + arr[-index])
            if middle_sum == arr[0]:
                return True
            else:
                return False
        else:
            even_index = int(len(arr)/2)
            if arr[even_index] == arr[0]:
                return True
            else:
                return False
    else:
        return False  

