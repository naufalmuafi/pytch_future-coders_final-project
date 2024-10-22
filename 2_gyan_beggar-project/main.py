import pytch
import random

score = 0
move_size = 20


class Bowl(pytch.Sprite):
    Costumes = ["bowl.png"]

    @pytch.when_green_flag_clicked
    def main(self):
        self.go_to_xy(0, -145)

    @pytch.when_key_pressed("ArrowLeft")
    def move_left(self):
        self.change_x(-move_size)

    @pytch.when_key_pressed("ArrowRight")
    def move_right(self):
        self.change_x(move_size)


class Money(pytch.Sprite):
    Costumes = ["money.jpg"]

    def drop(self, x, y):
        self.go_to_xy(x, y)
        global score

        # topik pemrograman 2: looping for
        # Using a for loop to simulate the falling motion
        for _ in range(y, -140, random.randint(-6, -3)):
            self.change_y(random.randint(-6, -3))
            # topik pemrograman 1: if
            if self.touching(Bowl):
                self.hide()
                score += 1
                break  # Stop the loop if it touches the bowl

    @pytch.when_green_flag_clicked
    def set_position(self):
        while True:
            self.show()
            self.drop(random.randint(-145, 190), random.randint(120, 150))


class City(pytch.Stage):
    Backdrops = ["city.jpg"]

    @pytch.when_green_flag_clicked
    def main(self):
        pytch.show_variable(None, "score")
