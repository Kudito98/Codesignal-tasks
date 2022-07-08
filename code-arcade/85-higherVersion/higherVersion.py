def solution(ver1, ver2):
    if ver1 == ver2:
        return False
    num1 = ver1.split(".")
    num2 = ver2.split(".")
    for i in range(len(num1)):
        if int(num1[i]) == int(num2[i]):
            continue
        elif int(num1[i]) > int(num2[i]):
            return True
        else:
            return False
