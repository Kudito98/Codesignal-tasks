def compose(functions):
    return (lambda f: f[0] if len(f) == 1 else (lambda x: f[0](compose(f[1:])(x))))(list(functions))

def solution(functions, x):
    return compose(map(eval, functions))(x)
