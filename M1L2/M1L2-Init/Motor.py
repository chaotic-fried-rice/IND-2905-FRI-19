class Motor:
  color = ""
  brand = ""
  speed = 0

  def __init__(self, color: str, brand: str = "Honda"):
    self.color = color
    self.brand = brand

  def gas(self, speed: int):
    self.speed += speed