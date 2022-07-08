def solution(value1, weight1, value2, weight2, maxW):
    max_val = 0
    if weight1 + weight2 <= maxW:
        max_val = value1 + value2   
        
    else:
        if weight1 <= maxW and weight2 <= maxW:
            max_val = max(value1,value2)
        elif weight1 <= maxW: 
            max_val += value1
        elif weight2 <= maxW:
            max_val += value2
    return max_val
    
