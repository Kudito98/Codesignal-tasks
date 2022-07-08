def solution(divisors, k):
    clan = []
    for i in range(1, k+1):
        vec = []
        for j in range(0,len(divisors)):
            if i % divisors[j] == 0:
                vec.append(1)
            else:
                vec.append(0)
        clan.append(vec)
    
    clanSet = []
    for i in range(0, len(clan)):
        if clan[i] not in clanSet:
            clanSet.append(clan[i])
    
    return len(clanSet)
