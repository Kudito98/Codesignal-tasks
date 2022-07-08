def solution(startTag):
    sT = (startTag.split(" "))[0][1::]
    if sT.endswith(">"):
        return "</" + sT
    else:
        return "</" + sT + ">"