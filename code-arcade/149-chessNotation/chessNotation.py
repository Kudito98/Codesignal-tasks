def solution(notation):
    return contract('/'.join(transpose(expand(notation).split('/'))))
    
def expand(notation):
    for i in range(1,9):
        notation = notation.replace(str(i),'1'*i)
    return notation

def contract(notation):
    for i in list(range(1,9))[::-1]:
        notation = notation.replace('1'*i,str(i))
    return notation

def transpose(ls):
    return [''.join(ls[i][j] for i in range(len(ls)))[::-1] for j in range(len(ls[0]))]
    