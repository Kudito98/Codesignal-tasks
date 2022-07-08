def solution(votes, k):
    count_winner = 0
    max_vote = max(votes)
    if k == 0 and votes.count(max_vote) == 1:
        return 1
    for vote in votes:
        if(vote + k > max_vote):
            count_winner += 1
    
    return count_winner
