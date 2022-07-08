def solution(address):
    domain = []
    for i in range(-1,-len(address)-1,-1):
        if address[i] != '@':
            domain.insert(0, address[i])
        else:
            break
    return "".join(domain)