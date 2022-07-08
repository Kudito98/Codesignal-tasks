def solution(upSpeed, downSpeed, desiredHeight):
    Dgrowth = upSpeed
    Ngrowth = upSpeed - downSpeed
    Day = 1
    while (Dgrowth or Ngrowth) < desiredHeight:
        Dgrowth += upSpeed - downSpeed
        Ngrowth += Dgrowth - downSpeed
        Day += 1
    return Day