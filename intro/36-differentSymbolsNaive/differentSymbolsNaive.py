def solution(s):
    letters = ""
    counter = 0
    for i in s:
        if i not in letters:
            letters += i
            counter += 1
    return counter