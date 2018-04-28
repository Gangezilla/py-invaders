class Player:
    def __init__(self):
        self.y_position = 550
        self.x_position = 400
        self.length = 60
        self.height = 30
        self.move_rate = 8
        self.id = 0

    def get_x_position(self):
        return self.x_position

    def set_x_position(self, new_x_position):
        self.x_position = new_x_position

    def get_y_position(self):
        return self.y_position

    def move_right(self):
        current_x = self.get_x_position()
        if 0 <= current_x <= 800:
            self.set_x_position(current_x + self.move_rate)
            print('moving right', current_x)

    def move_left(self):
        current_x = self.get_x_position()
        if 0 <= current_x <= 8000:
            self.set_x_position(current_x - self.move_rate)
            print('moving left', self.get_x_position())

    def shoot(self):
        print('shoot')

    def set_id(self, id):
        self.id = id
        print(self.id)

    def get_id(self):
        return self.id