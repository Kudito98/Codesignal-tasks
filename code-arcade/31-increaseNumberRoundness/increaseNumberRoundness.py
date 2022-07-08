def solution(n):
    while n % 10 == 0:
        n //= 10
    
    temp = 1
    while n:
        temp *= n%10
        n//=10
    
    if temp ==0:
        return True
    else:
        return False