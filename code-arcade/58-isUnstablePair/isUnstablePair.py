def solution(filename1, filename2):
    upperfilename1 = filename1.upper()
    lowerfilename1 = filename1.lower()
    
    upperfilename2 = filename2.upper()
    lowerfilename2 = filename2.lower()
    
    if upperfilename1<filename2 and lowerfilename1>filename2:
        if upperfilename2 < filename1 and lowerfilename2 > filename1:
            return True
        else:
            return False
    else:
        return False

