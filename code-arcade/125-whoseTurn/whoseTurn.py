def solution(p):
    if p == "b1;g1;b8;g8":
        return True
    p = p.split(";")
    white = 0
    black = 0
    if p[0]!="b1":
        s = p[0]
        temp = ord(s[0])-ord("b")+int(s[1])-1
        if temp%2!=0:
            white += 1
    if p[1]!="g1":
        s = p[1]
        temp = ord(s[0])-ord("g")+int(s[1])-1
        if temp%2!=0:
            white += 1
    if p[2]!="b8":
        s = p[2]
        temp = ord(s[0])-ord("b")+int(s[1])-8
        if temp%2!=0:
            black += 1
    if p[3]!="g8":
        s = p[3]
        temp = ord(s[0])-ord("g")+int(s[1])-8
        if temp%2!=0:
            black += 1

    if white%2==black%2:
        return True
    
    return False
