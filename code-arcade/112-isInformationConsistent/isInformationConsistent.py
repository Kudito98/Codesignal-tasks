def solution(evidences):
    for i in range(len(evidences[0])):
        info = 0
        for j in range(len(evidences)):
            if evidences[j][i]*info<0:
                return False
            else:
                info += evidences[j][i]
    return True
