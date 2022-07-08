def solution(formation, k):
    for i in range(k % 6):
        ghostPlayer = formation[3][2]
        formation[3][2] = formation[2][1]
        formation[2][1] = formation[3][0]
        formation[3][0] = formation[1][0] 
        formation[1][0] = formation[0][1]
        formation[0][1] = formation[1][2] 
        formation[1][2] = ghostPlayer
        
    return formation
        