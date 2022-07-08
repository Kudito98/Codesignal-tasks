def solution(rows):
    minTimer = len(rows)
    answer = []
    for i in range(len(rows[0])):
        finish = len(rows) - 1
        timer = 0
        for j in range(len(rows) - 1, -1, -1):
            if rows[j][i] == '#':
                timer = finish - j
                finish -= 1
        if timer == minTimer:
            answer.append(i)
        if timer < minTimer:
            minTimer = timer
            answer = [i]
    return answer
