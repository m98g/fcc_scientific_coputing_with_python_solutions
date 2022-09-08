class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return(f"Rectangle(width={self.width}, height={self.height})")

  def set_width(self, width):
    self.width = width
    
  def set_height(self, height):
    self.height = height

  def get_area(self):
    return(self.width * self.height)

  def get_perimeter(self):
    return((2 * self.width) + (2 * self.height))

  def get_diagonal(self):
    return((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    # lines are height and width the columns
    lines = []
    if self.width > 50 or self.height > 50:
      return("Too big for picture.")
    for i in range(self.height):
      lines.append("*" * self.width + "\n")
    # adds one \n too much
    return("".join(lines))

  def get_amount_inside(self, shape):
    width_shape, height_shape = shape.width, shape.height

    by_side = self.width // width_shape
    down = self.height // height_shape

    times = by_side * down
    
    return(times)


class Square(Rectangle):

  def __init__(self, length):
    self.length = length
    super().__init__(length, length)

  def __str__(self):
    return(f"Square(side={self.length})")

  def set_side(self, new_length):
    self.length = new_length
    self.set_width(new_length)

  # problem with this
  def set_width(self, width):
    self.length = width
    super().set_width(width)
    super().set_height(width)
    
  def set_height(self, height):
    self.length = height
    super().set_width(height)
    super().set_height(height)
    
