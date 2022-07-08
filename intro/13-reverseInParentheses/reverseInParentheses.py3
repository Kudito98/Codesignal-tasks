def solution(inputString):
    char = list(inputString)
    open_branket = []
    for i,c in enumerate(char):
        if c == '(':
            open_branket.append(i)
        elif c == ')':
            j = open_branket.pop()
            char[j:i] = char[i:j:-1]
    return ''.join(c for c in char if c not in'()')
            

