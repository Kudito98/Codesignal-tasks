import re
def solution(address):
    email_pattern = (r'@[A-Za-z0-9-]+\.[A-Z|a-z]{2,}\b')
    domain = ((re.findall(email_pattern, address))[0])[1::]
    return domain
