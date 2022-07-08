import re
def solution(inputString):
    addressMAC = re.findall(r'^(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})$', inputString)
    if addressMAC == []:
        return False
    else:
        return True