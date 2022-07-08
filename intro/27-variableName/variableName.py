def solution(name):
    if name[0].isdigit():
        return False
    else:  
        a = all([type(i) == str for i in name])
        b = all([i.isalpha() or i.isdigit() or i == '_' for i in name])
        
        return all([a,b])