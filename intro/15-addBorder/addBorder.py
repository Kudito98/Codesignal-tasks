def solution(picture):
    top_bottom_frame = ""
    framed_picture = list()

    for i in range(len(picture)):
        if i == 0:
            top_bottom_frame = '*' * (len(picture[0])+2)
            framed_picture.append(top_bottom_frame)

        framed_str = '*' + picture[i] + '*'
        framed_picture.append(framed_str)

        if i == len(picture)-1:
            top_bottom_frame = '*' * (len(picture[0])+2)
            framed_picture.append(top_bottom_frame)

    return framed_picture

