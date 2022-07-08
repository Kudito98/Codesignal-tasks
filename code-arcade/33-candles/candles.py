def solution(candlesNumber, makeNew):
    leftovers = 0
    burnedCandles = 0
    while candlesNumber != 0:
        burnedCandles += candlesNumber
        leftovers += candlesNumber
        candlesNumber = leftovers // makeNew
        leftovers -= candlesNumber * makeNew
    return burnedCandles
         
        
