def solution(a, b):
    intlist = [a]
    while a != b:
        a += 1
        intlist.append(a)
        
    binlist = [bin(i)[2::] for i in intlist]
    stvals = ""
    for i in binlist:
        stvals += i
    return stvals.count("1")
