import tkinter as tk

class Bullet:
  def __init__(self, creator, origin_x, origin_y, canvas, root):
    self.canvas = canvas
    self.speed = -10
    self.height = 25
    self.creator = creator
    self.root = root
    self.origin_x = origin_x
    self.origin_y = origin_y
    self.bullet = canvas.create_line(
      origin_x,
      origin_y,
      origin_x,
      origin_y - self.height
    )
    self.active = True
    self.move()

  def update(self):
    self.canvas.move(self.bullet, 0, self.speed)

  def move(self):
    # check if its in bounds, might have to deal with objects going out of bounds???
    # if not in bounds, self.canvas.delete(self.bullet)
    if self.active:
      self.update()
      self.root.after(10, self.move)

