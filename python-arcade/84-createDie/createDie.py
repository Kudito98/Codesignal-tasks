import random

def solution(seed, n):
    class Die(object):
        def __new__(*args):
            return int(random.Random(seed).random()*n)+1

    class Game(object):
        die = Die(seed, n)

    return Game.die
