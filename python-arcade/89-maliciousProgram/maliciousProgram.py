import datetime, time

def solution(curDate, changes):
    formatting = '%d %b %Y %H:%M:%S'
    current = time.strptime(curDate, formatting)
    changes[0], changes[2] = changes[2], changes[0]
    try:
        return datetime.datetime(*(current[i]+changes[i] for i in range(6))).strftime(formatting)
    except ValueError:
        return curDate