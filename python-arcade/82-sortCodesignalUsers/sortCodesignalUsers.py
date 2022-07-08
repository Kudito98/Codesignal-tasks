def solution(users):
    res = [CodeSignalUser(*user) for user in users]
    res.sort(reverse=True)
    return list(map(str, res))

class CodeSignalUser(object):
    def __init__(self, *args):
        self.username = args[0]
        self.id = int(args[1])
        self.xp = int(args[2])
    
    def __lt__(self, user):
        return self.xp < user.xp or (self.xp == user.xp and self.id > user.id)
        
    def __str__(self):
        return self.username