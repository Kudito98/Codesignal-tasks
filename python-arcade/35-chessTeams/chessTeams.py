def solution(smarties, cleveries):
    return [[smarties[n]] +[cleveries[n]] for n in range(len(cleveries))]
