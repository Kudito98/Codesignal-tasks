def solution(text):
    words = ""
    for i in text:
        if i.isalpha() or i == " ":
            words += i
        else:
            words += " " 
    lstwords = words.split(" ")
    mlen = ""
    for i in lstwords:
        if len(i) > len(mlen):
            mlen = i
    return mlen