def solution(array1, array2):
    
    if len(array1) != len(array2):
        return False
    
    lenghtArr1 = [len(i) for i in array1]
    lenghtArr2 = [len(j) for j in array2]
    
    return sum(lenghtArr1) == sum(lenghtArr2)
