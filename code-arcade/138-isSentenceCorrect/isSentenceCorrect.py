def solution(sentence):
    pattern = r'^[A-Z][^/.?!]*[.?!]$'  
    return re.match(pattern, sentence) is not None
