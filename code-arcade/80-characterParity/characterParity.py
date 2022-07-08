def solution(symbol):
    ans = ("even", "odd", "not a digit")
    if symbol.isdigit():
        if int(symbol) % 2 == 0:
            return ans[0]
        else:
            return ans[1]
    else:
        return ans[2]
