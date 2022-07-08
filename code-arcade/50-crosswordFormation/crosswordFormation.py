import itertools

def Iteration(fWord, sWord, tWord, foWord):
    count = 0
    
    for i in range(len(fWord) - 2):
        for k in range(len(tWord) - 2):
            if(fWord[i] == tWord[k]):
                
                for j in range(i+2, len(fWord)):
                    for l in range(len(foWord) - 2):
                        
                        if(fWord[j] == foWord[l]):
                            hPoint = j - i
                            vPoint = l - k
                            
                            for p in range(len(sWord) - hPoint):
                                for q in range(k+2, len(tWord)):
                                    if(len(foWord) > q + vPoint):
                                        if(sWord[p] == tWord[q] and sWord[p + hPoint] == foWord[q + vPoint]):
                                            count += 1

    return count

def solution(words):
    res = 0
    permWords = sorted(tuple(itertools.permutations(words, 4)))
    
    for oneLineWords in permWords:
        res += Iteration(oneLineWords[0], oneLineWords[1], oneLineWords[2], oneLineWords[3])
    
    return res
    
    
                