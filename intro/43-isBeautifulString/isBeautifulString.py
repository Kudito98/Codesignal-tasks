def solution(inputString):
    temp_dict = dict()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        temp_dict[char] = 0
    for char in inputString:
        temp_dict[char] = temp_dict.get(char) + 1
        prev_val= temp_dict['a']
        alphabet = 'bcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if temp_dict[char] > prev_val:
            return False
        prev_val = temp_dict[char]
    return True
