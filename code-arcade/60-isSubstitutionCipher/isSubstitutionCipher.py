def solution(string1, string2):
    return len(set(zip(string1, string2))) == len(set(string1)) == len(set(string2))