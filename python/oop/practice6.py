class Rectangle:
    def __init__(self, width, height):
        self._width = width  # Atribut privat

    @property
    def width(self):
        return self._width  # Getter untuk atribut _width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value  # Setter untuk atribut _width
        else:
            raise ValueError("Width harus lebih besar dari 0")

rectangle = Rectangle(5, 10)
print(rectangle.width)  # Output: 5
rectangle.width = 8
print(rectangle.width)  # Output: 8
