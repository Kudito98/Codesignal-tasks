def rotate(move, faces):
    face1, face2, face3 = faces
    face1[0], face2[4], face3[8] = face2[4], face3[8], face1[0]
    if move.islower():
        face1[1], face2[6], face3[3] = face2[6], face3[3], face1[1]
        face1[2], face2[5], face3[7] = face2[5], face3[7], face1[2]
        face1[3], face2[1], face3[6] = face2[1], face3[6], face1[3]
    return [face1, face2, face3]
        

def solution(faceColors, moves):
    front, bottom, left, right = [[color for _ in range(9)] for color in faceColors]
    for move in moves[::-1]:
        corner = move[0].upper()
        if corner == "U":
            faces = [front, left, right]
        if corner == "R":
            faces = [right, bottom, front]
        if corner == "L":
            faces = [left, front, bottom]
        if corner == "B":
            faces = [bottom, right, left]
        faces = rotate(move[0], faces)
        if len(move) == 1:
            faces = rotate(move[0], faces)
    return [front, bottom, left, right]
