def solution(picture):
    pictureLenght = len(picture[0]) + 2
    stars = '*'*pictureLenght
    frame = [stars]
    
    for i in range(len(picture)):
        row = "*" + picture[i] + "*"
        frame.append(row)
    
    frame.append(stars)
    return frame
    
