def solution(x, functions):
    return list(eval('(' + func + ')' + '('+ str(x) +')') for func in functions)
