def solution(names): 
    for i in range(len(names)):
    #if name already exist in the list
        if names[i] in names[:i]:
            count = 1
            #count keep increase until name (#) is exist in the list
            while names[i]+"("+str(count)+")" in names [:i]:
                count+=1
            #replace the new name (#) to the list with the current value
            names[i]+="("+str(count)+")"
    return names