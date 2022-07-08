import urllib.parse as parse

def solution(url1, url2):
    url_1 = parse.urlparse(url1)
    url_2 = parse.urlparse(url2)
    similarity = 0 
    
    if url_1.scheme == url_2.scheme:
        similarity += 5
        
    if url_1.netloc == url_2.netloc:
        similarity += 10
    
    path_component_1 = url_1.path.split('/')[1:]
    path_component_2 = url_2.path.split('/')[1:]

    for e1,e2 in zip(path_component_1, path_component_2):
        if e1 == e2:
            similarity += 1
        else:
            break
    k1 = parse.parse_qs(url_1.query)
    k2 = parse.parse_qs(url_2.query)
    similarity += len(k1.keys() & k2.keys())
    
    for keys in (k1.keys() & k2.keys()):
        if k1[keys] == k2[keys]:
            similarity += 1
    
    return similarity