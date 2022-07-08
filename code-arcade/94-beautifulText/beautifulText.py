def solution(inputString, l, r):
    size = len(inputString)
    for width in range(l,r+1):
        if size%(width+1)==width:
            beautiful = True
            for i in range(0,(size+1)//(width+1)-1):
                if inputString[(i+1)*(width+1)-1]!=" ":
                    beautiful = False
                    break
            if beautiful:
                return True
            
    return False
