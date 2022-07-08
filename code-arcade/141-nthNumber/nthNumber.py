def solution(s, n):
    pattern = r"(?:[^1-9]*(\d+)){"+str(n)+"}"
    return re.match(pattern, s).group(1)
