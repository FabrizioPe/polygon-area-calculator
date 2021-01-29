class Rectangle:
    """A class representing a rectangle."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        if width > 0: self.width = width;
        else: print("Error: side length must be positive.")

    def set_height(self, height):
        if height > 0: self.height = height;
        else: print("Error: side length must be positive.")

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        """Return a graphical representation of the rectangle."""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ('*' * self.width + '\n') * self.height

    def get_amount_inside(self, shape):
        """Calculate how many "shape"s fit inside the rectangle."""
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle class."""

    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, side):
        super().set_width(side)
        super().set_height(side)

    def set_height(self, side):
        super().set_height(side)
        super().set_width(side)

    def set_side(self, side):
        super().set_height(side)
        super().set_width(side)

    def __str__(self):
        return f"Square(side={self.width})"
