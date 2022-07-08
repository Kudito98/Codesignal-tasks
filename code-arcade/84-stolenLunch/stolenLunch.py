def solution(note):
    decipherNote = ""
    for i in note:
        if i.isdigit():
            decipherNote += str(chr(int(i)+97))
        elif ord(i) <= 106 and ord(i) >= 97:
            decipherNote += str(ord(i) - 97)
        else:
            decipherNote += i
    return decipherNote