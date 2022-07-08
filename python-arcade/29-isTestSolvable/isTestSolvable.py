def solution(ids, k):
    digitSum = lambda sumowanko: sum(int(x) for x in str(sumowanko))

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0
