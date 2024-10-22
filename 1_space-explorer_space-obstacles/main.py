import pytch
import random

x_border = 220


class Rocket(pytch.Sprite):
    Costumes = ["rocket.png"]
    direction = 3

    @pytch.when_green_flag_clicked
    def main(self):
        self.go_to_xy(0, -145)

        while True:
            self.change_x(self.direction)

            if self.x_position > x_border:
                self.direction *= -1
            elif self.x_position < -x_border:
                self.direction *= -1

    @pytch.when_I_receive("belok")
    def change_the_direction(self):
        # Reverse the direction
        self.direction *= -1

    @pytch.when_I_receive("gameover")
    def stop_game(self):
        self.direction = 0
        self.say_for_seconds("Game Over", 3)
        pytch.stop_all()


class Meteor(pytch.Sprite):
    Costumes = ["meteor.png"]
    game_over = False

    def drop(self, x, y):
        self.go_to_xy(x, y)
        global score

        while self.y_position > -140 and not self.game_over:
            self.change_y(random.randint(-6, -3))
            if self.touching(Rocket):
                pytch.broadcast("gameover")
                self.game_over = True

    @pytch.when_green_flag_clicked
    def set_position(self):
        while not self.game_over:
            self.show()
            self.drop(random.randint(-145, 190), random.randint(120, 150))


class Space(pytch.Stage):
    Backdrops = ["space.jpg"]

    @pytch.when_stage_clicked
    def broadcast(self):
        pytch.broadcast("belok")
