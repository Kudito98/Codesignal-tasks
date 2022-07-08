import re
def solution(maxLength, text):
    text = re.split('\W+',text)
    return len([i for i in text if len(i)<=maxLength and i !="" and not '0'<=i<='9'])