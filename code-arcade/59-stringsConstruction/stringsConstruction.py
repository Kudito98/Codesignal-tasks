def solution(a, b):
    cntA = count(a)
    cntB = count(b)
    best = -1
    for i in range(26):
        if cntA[i] == 0:
            continue
        cur = cntB[i] / cntA[i]
        if best == -1 or cur < best:
            best = cur
    return int(best)

def count(s):
    cnt = [0 for i in range(26)]
    for i in range(len(s)):
        cnt[ord(s[i]) - ord('a')] += 1
    return cnt