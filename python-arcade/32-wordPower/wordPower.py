def solution(word):
    num = {w: ord(w)-96 for w in word}
    return sum([num[ch] for ch in word])
