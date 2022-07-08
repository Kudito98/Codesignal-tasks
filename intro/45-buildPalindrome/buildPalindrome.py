def isPalindrom(st):
    return st == st[::-1]

def solution(st):
    for i in range(len(st)):
        substracting = st[i::]
        if isPalindrom(substracting):
            nonPalindrom = st[:i]
            return st + nonPalindrom[::-1]