def solution(expr):
    priority = 1
    v = []
    for i in range(len(expr)):
        if expr[i] == '(':
            priority += 2
        elif expr[i] == ')':
            priority -= 2
        else:
            if expr[i] == '+' or expr[i] == '-':
                v.append((i, priority + 1))
            elif expr[i] == '*' or expr[i] == '/':
                v.append((i, priority + 2))
    
    res = 0
    maxPriority = 0
    for j in v:
        if maxPriority < j[1]:
            res = j[0]
            maxPriority = j[1]

    return res
