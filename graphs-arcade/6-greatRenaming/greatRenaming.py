def solution(roadRegister):
    return [[i[-1]] + i[:-1] for i in [roadRegister[-1]] + roadRegister[:-1]]