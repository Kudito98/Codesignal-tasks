def solution(s):
    lenS = len(s)
    for i in range(0,lenS):
        sub = s[0:i+1]
        times = lenS // (i + 1)+ 1
        if s in sub*times:
            return i+1
