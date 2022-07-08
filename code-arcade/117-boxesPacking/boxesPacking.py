def solution(length, width, height):
    L, W, H = length, width, height
    dimensions = []
    for i in range(len(L)):
        dimensions.append(sorted([L[i],W[i],H[i]]))
        
    dimensions = sorted(dimensions,key = lambda x: (x[0],x[1],x[2]))
    
    for i in range(len(L)-1):
        if dimensions[i][0]>= dimensions[i+1][0] or dimensions[i][1]>= dimensions[i+1][1] or dimensions[i][2]>= dimensions[i+1][2]:
            return False
        
    return True

