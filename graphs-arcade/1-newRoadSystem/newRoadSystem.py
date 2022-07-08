def solution(roadRegister):
    for x, y in zip(map(sum, roadRegister), map(sum, zip(*roadRegister))):
        print(x, y)
        if x != y:
            return False
    return True
