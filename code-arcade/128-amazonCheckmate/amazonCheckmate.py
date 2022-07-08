from itertools import count, product
from typing import NamedTuple


class Position(NamedTuple):
    x: int
    y: int

    @classmethod
    def parse(cls, s):
        return cls(*(ord(c) - ord(b) for c, b in zip(s, "a1")))
    
    
    def in_bounds(self):
        return 0 <= self.x < 8 and 0 <= self.y < 8
    
    
def solution(king, amazon):
    king, amazon = map(Position.parse, [king, amazon])
    results = [0] * 4
    king_moves = set(neighbours(king))
    amazon_moves = set(get_amazon_moves(amazon, king))
    for position in all_positions():
        if (
            position != amazon and
            position != king and
            position not in king_moves
        ):
            results[check(position, king_moves, amazon_moves)] += 1
    return results


def all_positions():
    return (
        Position(x, y)
        for x, y in product(range(8), repeat=2)
    )

    
def get_amazon_moves(amazon, king):
    for dx, dy in product([-2, -1, 1, 2], repeat=2):
        if abs(dx) != abs(dy):
            move = Position(amazon.x + dx, amazon.y + dy)
            if move.in_bounds():
                yield move
    for dx, dy in product([-1, 0, 1], repeat=2):
        if not dx == dy == 0:
            for position in map(Position, count(amazon.x + dx, dx), count(amazon.y + dy, dy)):
                if not position.in_bounds() or position == king:
                    break
                yield position


def neighbours(position):
    for dx, dy in product([-1, 0, 1], repeat=2):
        neighbor = Position(position.x + dx, position.y + dy)
        if neighbor.in_bounds() and neighbor != position:
            yield neighbor
    
    
def check(position, king_moves, amazon_moves):
    not_under_attack = position not in amazon_moves
    can_move = any(
        n not in king_moves and n not in amazon_moves
        for n in neighbours(position)
    )
    return not_under_attack * 2 + can_move