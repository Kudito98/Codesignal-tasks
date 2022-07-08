def solution(vines, n):
    def nTimes(n):
        def decorator(func):
            def wrapper(bottles):
                res = bottles
                for i in range(n):
                    res = func(res)
                return res
            return wrapper
        return decorator 

    @nTimes(n)
    def sumOnce(vines):
        res = [vines[i] + vines[i + 1] for i in range(0, len(vines) - 1, 2)]
        if len(vines) % 2 == 1:
            res.append(vines[-1])
        return res

    return sumOnce(vines)
