EMPTY = '.'
BODY = '*'
DEAD = 'X'
HEADS = {'v': (1, 0), '^': (-1, 0), '<': (0, -1), '>': (0, 1)}

class Snake(object):
    # Heads and body parts are (x, y, char)
    def __init__(self, head, dimx, dimy):
        self.dimx = dimx
        self.dimy = dimy
        self.body = [head]
        self.alive = True

    def add_queue(self, body_part):
        self.body.append(body_part)

    def turn(self, direc):
        new_direc = {'v': {'L': '>', 'R': '<'}, 
                     '^': {'L': '<', 'R': '>'},                 
                     '<': {'L': 'v', 'R': '^'}, 
                     '>': {'L': '^', 'R': 'v'}}
        x, y, head = self.body[0]
        new_head = new_direc[head][direc]
        self.body[0] = (x, y, new_head)

    def move_forward(self):
        x, y, char = self.body[0]
        dx, dy = HEADS[char]
        new_x, new_y = x + dx, y + dy
        if self.position_is_free(new_x, new_y): 
            self.body = [(new_x, new_y, char)] + [(x, y, BODY)] + self.body[1:-1]
        else:
            self.die()

    def position_is_free(self, x, y):
        return x in range(self.dimx) and \
               y in range(self.dimy) and \
               not any(x == x2 and y == y2 for (x2, y2, _) in self.body)

    def die(self):
       self.alive = False
       self.body = [(x, y, DEAD) for (x, y, _) in self.body] 

    def get_as_grid(self):
        g = [[EMPTY for i in range(self.dimy)] for j in range(self.dimx)]
        for x, y, c in self.body:
            g[x][y] = c
        return g

def find_head(gameBoard):
    for i, row in enumerate(gameBoard):
        for head, (dx, dy) in HEADS.items():
            if head in row:
                return Snake((i, row.index(head), head), len(gameBoard), len(gameBoard[0]))


def get_next(snake, gameBoard):
    x, y, _ = snake.body[-1]
    for (dx, dy) in HEADS.values():
        new_x, new_y = x + dx, y + dy
        if snake.position_is_free(new_x, new_y) and \
           gameBoard[new_x][new_y] == BODY:
            return (new_x, new_y, BODY)


def find_snake(gameBoard):
    # Get the head
    s = find_head(gameBoard)

    # Append the rest of the body
    while True:
        n = get_next(s, gameBoard)
        if n is None:
            break
        s.add_queue(n)
    return s


def solution(gameBoard, commands):
    # Find snake
    s = find_snake(gameBoard)

    for command in commands:
        if command in "LR":
            # Change the head
            s.turn(command)
        else:
            s.move_forward()
            if not s.alive:
                break  
    return s.get_as_grid()