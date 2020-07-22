class Circle:
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f'A circle of radius {self.radius}'


class Square:
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'A square of side {self.side}'


class ColoredShape:
    def __init__(self, shape, color):
        self.color = color
        self.shape = shape

    def resize(self, factor):
        resize_method = getattr(self.shape, 'resize', None)
        if resize_method and callable(resize_method):
            return self.shape.resize(factor)
        else:
            self.shape.side *= factor

    def __str__(self):
        return f'{self.shape} has the color {self.color}'


if __name__ == '__main__':
    circle = ColoredShape(Circle(5), 'red')
    print(str(circle))

    circle.resize(2)
    print(str(circle))
