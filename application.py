import tkinter as tk
from player import Player
from bullet import Bullet
from barrier import Barrier


class Application:
    def __init__(self):
        print('app init, innit')
        self.player = Player()
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        player_id = self.draw_player()
        self.draw_barriers()
        self.player.set_id(player_id)
        self.canvas.bind("<Key>", self.key)
        self.canvas.focus_set()
        self.root.mainloop()

    def draw_player(self):
        player_x = self.player.get_x_position()
        player_y = self.player.get_y_position()
        print(self.player.length)
        id = self.canvas.create_rectangle(
            player_x,
            player_y,
            player_x - self.player.length,
            player_y - self.player.height,
        )
        return id

    def move_player(self):
        player_x = self.player.get_x_position()
        player_y = self.player.get_y_position()
        player_id = self.player.get_id()
        self.canvas.coords(
            player_id,
            player_x,
            player_y,
            player_x - self.player.length,
            player_y - self.player.height,
        )

    def key(self, event):
        key = event.keysym
        if key == "Right":
            self.player.move_right()
            self.move_player()
        if key == "Left":
            self.player.move_left()
            self.move_player()
        if key == 'space':
            self.player_shoot()

    def player_shoot(self):
        origin_x = self.player.get_x_position() - (self.player.length / 2)
        origin_y = self.player.get_y_position() - self.player.height
        Bullet('player', origin_x, origin_y, self.canvas, self.root)

    def draw_barriers(self):
        Barrier(250, self.canvas)
        Barrier(550, self.canvas)