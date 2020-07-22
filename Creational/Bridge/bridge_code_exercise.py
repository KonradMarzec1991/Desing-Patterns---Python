from abc import ABC


class Renderer(ABC):
    def what_to_render_as(self, name):
        pass


class VectorRenderer(Renderer):
    def what_to_render_as(self, name):
        return f'Drawing {name} as lines'


class RasterRenderer(Renderer):
    def what_to_render_as(self, name):
        return f'Drawing {name} as pixels'


class Shape:
    def __init__(self, renderer):
        self.renderer = renderer


class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = 'Triangle'

    def __str__(self):
        return self.renderer.what_to_render_as(self.name)


class Square(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = 'Square'

    def __str__(self):
        return self.renderer.what_to_render_as(self.name)


if __name__ == '__main__':
    print(str(Triangle(RasterRenderer())))
    print(str(Square(VectorRenderer())))
