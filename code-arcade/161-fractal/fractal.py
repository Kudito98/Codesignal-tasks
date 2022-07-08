rot=lambda s: map(lambda x:(x+1)%4,s)
flip=lambda s: map(lambda x:4-x if x % 2 else x,s)

DIRS=[(0,1),(-1,0),(0,-1),(1,0)]
def solution(n):
    F=[]
    for x in range(n):
        F1=[*flip(rot(F))]
        F2=[*rot(rot(F))]
        a,b,c= (3,0,1) if x%2 else (0,3,2)
        F=F+[a]+F1+[b]+F1+[c]+F2
    L=2**n
    l=2*L-1
    ret=[[' ']*l for x in range(L)]
    px,py=0,0
    prev=-1
    for d in F:
        dx,dy=DIRS[d]
        if d==prev and d%2==0:
            ret[px][py]='_'
        if d!=1:
                    px+=dx
                    py+=dy
        ret[px][py]='|' if d%2 else '_'
        if dy or d==1:
            px+=dx
            py+=dy
        prev=d
    return ret
