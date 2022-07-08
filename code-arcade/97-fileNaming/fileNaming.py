def solution(names):
    fileNames = []
    for name in names:
        if name in fileNames:
            name = name + '(1)'
            while name in fileNames:
                name = name[:-2] + str(int(name[-2]) + 1) + ')'
            fileNames.append(name)
        else:
            fileNames.append(name)
    return fileNames
