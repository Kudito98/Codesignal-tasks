def solution(score1, score2):
    highscore = max(score1, score2)
    minscore = min(score1, score2)

    if highscore == 6 and minscore < 5:
        return True
    elif highscore == 7 and (minscore == 5 or minscore == 6):
        return True

    return False