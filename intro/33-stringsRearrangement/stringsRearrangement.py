import itertools
def solution(inputArray):
    
    for perm in itertools.permutations(inputArray):
        if _consecutive_strings_differ_by_one_character(perm):
            return True
    return False


def _consecutive_strings_differ_by_one_character(inputArray: list):
    iter_input_array = inputArray[:-1]
    for i, current_str in enumerate(iter_input_array):
        next_str = inputArray[i + 1]
        if not _differ_by_one_char(current_str, next_str):
            return False
    return True


def _differ_by_one_char(str1: str, str2: str):
    result = False
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            if result:
                return False
            else:
                result = True
    return result
