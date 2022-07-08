from re import findall
def solution(s1, s2):
     regex = r'[A-Za-z]|\d+'
     s1 = [(0, int(f), -f.count('0')) if f.isdigit() else (1, f) for f in findall(regex, s1)]
     s11 = [f[:2] for f in s1]
     s2 = [(0, int(f), -f.count('0')) if f.isdigit() else (1, f) for f in findall(regex, s2)]
     s21 = [f[:2] for f in s2]
     return (s11 < s21) or ((s11 == s21) and (s1 < s2))
