class Rectangle(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__(self):
        return '{} x {} = {}'.format(self.height, self.width, self.area)

    def get_area(self):
        return self.height * self.width
        
    area = property(fget=get_area)


def solution(height, width):
    return str(Rectangle(height, width))
