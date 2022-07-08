def solution(lrcLyrics, songLength):
    res = []   
    for i, l in enumerate(lrcLyrics, 1):
        sep = l.index(']')
        t, tf = l[1:sep].split(".")
        m, s = map(int, t.split(':'))
        h, m = divmod(m, 60)
        ct = "{:02}:{:02}:{:02},{}0".format(h, m, s, tf)
        
        if i > 1:
            res[-2] += ct
            res.append("")
        res.extend([str(i), ct + " --> ", l[sep + 2:]])
    res[-2] += songLength + ',000'
    return res
        
