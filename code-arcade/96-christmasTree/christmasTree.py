def solution(levelNum, levelHeight):
    maxW = 5+(levelHeight-1)*2
    width = 5+(levelHeight-1)*2+(levelNum-1)*2
    crown = [" "*int((width-1)//2)+"*"," "*int((width-1)//2)+"*"," "*int(((width-1)/2-1))+"***"]
    tree = crown
    
    for i in range(levelNum):
        for j in range(5+i*2,maxW+i*2+1,2):
            space = " "*((width-j)//2)
            line = space+"*"*j
            tree.append(line)
    
    if levelHeight%2==0:
        foot = "*"*(levelHeight+1)
    else:
        foot = "*"*levelHeight
    foot = " "*((width-len(foot))//2)+foot
    for i in range(levelNum):
        tree.append(foot)
    return tree
