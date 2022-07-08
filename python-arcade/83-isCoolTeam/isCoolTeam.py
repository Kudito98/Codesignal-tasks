class Team(object):
    def __init__(self, names):
        self.names = names

    def __bool__(self):
        self.names = [i.lower() for i in self.names]

        letters = "abcdefghijklmnopqrstuvwxyz"
        FROM  = {i: [] for i in letters}
        TO    = {i: [] for i in letters}

        for i in letters:
            for j in self.names:
                if i == j[-1]:
                    FROM[i].append(j)
                if i == j[0]:
                    TO[i].append(j)

        start = False
        end   = False
        for i in letters:
            if len(FROM[i]) + 1 == len(TO[i]):
                if start:
                    return False 
                start = True
            elif len(FROM[i]) == len(TO[i]) + 1:          
                if end:
                    return False 
                end = True
            elif len(FROM[i]) != len(TO[i]):
                return False

        visited = {0}
        queue = [0]

        while queue:

            name = queue.pop(0)
            for ind, teammate in enumerate(self.names):
                if ind in visited:
                    continue
                if self.names[name][0] == teammate[-1]:
                    visited.add(ind)
                    queue.append(ind)
                elif self.names[name][-1] == teammate[0]:
                    visited.add(ind)
                    queue.append(ind)

        return len(visited) == len(self.names)

def solution(team):
    return bool(Team(team))
