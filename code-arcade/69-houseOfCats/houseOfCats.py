def solution(legs):
    maxCats = legs//4
    res = []
    for i in range(maxCats+1):
        people = (legs-i*4)//2
        res.insert(0, people)
        
    return res
    
        