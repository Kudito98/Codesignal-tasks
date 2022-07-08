def solution(roadRegister):
    n = len(roadRegister)
    newRegister = []
    newRegister = [[[roadRegister[j][k] for j in range(n) if j!=l]for k in range(n) if k!=l] for l in range(n)] 
    return newRegister
