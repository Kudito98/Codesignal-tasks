import re
def solution(inputString):
    IP = [inputString.split(".") if inputString.count(".") <= 3 else []][0]
    mylist = [i for i in IP if i.isdigit()]
    
    if len(mylist) < 4:
        return False
    for i in mylist:
        if i.startswith("00") or i.startswith("01"):
            return False
        elif(int(i) > 255):
            return False
        else:
            continue
    return True
