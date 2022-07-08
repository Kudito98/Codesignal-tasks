def solution(size, nonogramField):
    sep = int((size+1)/2)
    rows = nonogramField[sep:]
    columns = list(zip(*nonogramField))[sep:]
    return all(test(row, sep) for row in rows) and all(test(list(col), sep) for col in columns)

def test(vect, sep):
    hashes = vect[sep:]
    tempList = []
    n = 0
    for c in hashes:
        if c == "#":
            n += 1
        elif n != 0:
            tempList.append(str(n))
            n = 0
    if n != 0:
        tempList.append(str(n))
    print(tempList, vect[sep-len(tempList):sep])
    return tempList == vect[sep-len(tempList):sep]