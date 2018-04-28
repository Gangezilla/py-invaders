class Barrier:
    def __init__(self, origin_x, canvas):
        self.origin_x = origin_x
        self.canvas = canvas
        self.origin_y = 475
        self.width = 60
        self.height = 40
        self.canvas.create_rectangle(
            self.origin_x,
            self.origin_y,
            self.origin_x - self.width,
            self.origin_y - self.height
        )