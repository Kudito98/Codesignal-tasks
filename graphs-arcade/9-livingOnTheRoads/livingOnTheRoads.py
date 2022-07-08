def solution(roadRegister):
    roReg = []
    for i in range(len(roadRegister)):
        for j in range(len(roadRegister)):
            if roadRegister[i][j] == True and roadRegister[j][i] == True:
                if (j, i) not in roReg:
                    roReg.append((i, j))

    return [[i!=j and bool(set(i) & set(j)) for j in roReg] for i in roReg]