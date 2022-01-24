from abc import ABC, abstractmethod

class Shape(ABC):
  
  @abstractmethod
  def set_width(self, width):
    pass
  
  @abstractmethod
  def set_height(self, height):
    pass
  @abstractmethod
  def get_area(self):
    pass
  @abstractmethod
  def get_perimeter(self):
    pass
  


class Rectangle(Shape):

  def __init__(self, width, height):
    self.set_width(width)
    self.set_height(height)

  def set_width(self, width):
    self.width = width
  
  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height
  
  def get_perimeter(self):
    return (2*self.width) + (2*self.height)
  
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5
  
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    return '\n'.join([''.join(['*' for i in range(self.width)]) for a in range(self.height)])+"\n"

  def get_amount_inside(self, shape):
    return (int(self.width/shape.width) * int(self.height/shape.height))

  def __repr__(self):
    return f"Rectangle(width={str(self.width)}, height={str(self.height)})"
    

class Square(Rectangle):
  def __init__(self, length):
    self.set_side(length)

  def set_side(self, length):
    self.set_height(length)
    self.set_width(length)
  
  def __repr__(self):
    return f"Square(side={self.width})"
