def solution(code):
    res = ""
    for i in range(0, len(code), 8):
        num = int(code[i:i+8], 2)
        res += chr(num)
    return res