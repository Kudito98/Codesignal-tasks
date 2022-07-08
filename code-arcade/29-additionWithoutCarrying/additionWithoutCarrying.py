def solution(param1, param2):
    biggerP = max(param1, param2)
    lowerP = min(param1, param2)
    sbp = str(biggerP)[::-1]
    slp = str(lowerP)[::-1]
    nslp = ""
    
    if len(sbp) > len(slp):
        mltp = len(sbp) - len(slp)
        addzero = mltp * "0"
        nslp = slp + addzero
    else:
        nslp = slp
    
    AValue = ""
    for i in range(len(nslp)):
        DigitSum = int(sbp[i]) + int(nslp[i])
        if DigitSum >= 10:
            DigitSum -= 10
            AValue += str(DigitSum)
        else:
            AValue += str(DigitSum)
    
    Sval = AValue[::-1]
    Finalvalue = int(Sval)
    return Finalvalue