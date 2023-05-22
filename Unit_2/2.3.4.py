class Pixel:
    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        average_color = (self._red + self._green + self._blue) // 3
        self._red = average_color
        self._green = average_color
        self._blue = average_color

    def print_pixel_info(self):
        color = f"({self._red}, {self._green}, {self._blue})"
        if self._red == 0 and self._green == 0 and self._blue > 50:
            color += " Blue"
        elif self._red == 0 and self._green > 50 and self._blue == 0:
            color += " Green"
        elif self._red > 50 and self._green == 0 and self._blue == 0:
            color += " Red"

        print(f"X: {self._x}, Y: {self._y}, Color: {color}")


# Main program
p = Pixel(5, 6, 250)
p.print_pixel_info()
p.set_grayscale()
p.print_pixel_info()
