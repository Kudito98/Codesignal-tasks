class Prizes(object):
    def __init__(self, purchases, n, d):
        self.purchases = purchases
        self.n = n
        self.d = d
    
    def __iter__(self):
        for i, x in enumerate(self.purchases):
            if (i+1) % self.n == 0 and x % self.d == 0:
                yield i + 1 

def solution(purchases, n, d):
    return list(Prizes(purchases, n, d))
