def solution(coins, price):
    spentCoins = 0
    for i in reversed(coins):
        if price > 0:
            cc = price // i
            price -= i * cc
            spentCoins += cc
    return spentCoins