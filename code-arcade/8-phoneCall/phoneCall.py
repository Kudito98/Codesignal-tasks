def solution(min1, min2_10, min11, s):
    callmin = 0
    costcall = 0
    if (min1 <= s) & (min2_10 <= s) & (min11 <= s):
        while costcall <= s:
            callmin += 1
            if  callmin <= 1:
                s -= min1
                continue
            elif callmin <= 10:
                s -= min2_10
                continue
            else:
                s -= min11
                continue
            break
        return (callmin - 1)
    else:
        return callmin
                
        
            
            
            
