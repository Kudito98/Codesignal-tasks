from collections import Counter
def solution(n):
    sequence = [n]
    while n:
        nStr = str(n)
        digitSum = 0
        for i in nStr:
            digitSum += int(i)
        n -= digitSum
        sequence.append(n)
    
    sumSequence = []
    for i in sequence:
        sumJ = 0
        for j in str(i):
            sumJ += int(j)
        sumSequence.append(sumJ)
        
    occurence_count = Counter(sumSequence)
    return max([s for s ,count in occurence_count.most_common() if count==occurence_count.most_common(1)[0][1]])
    
        
