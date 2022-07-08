def solution(s):
    return re.sub(r'(\w+) (\w+)', r'\2 \1', s) 
