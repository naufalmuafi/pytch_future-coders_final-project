import pytch
import random

# select level: easy/medium/hard
level = "easy"

move_size = 20


class Peluru(pytch.Sprite):
    Costumes = ["bullet.png"]
    game_over_peluru = False
    win = False

    @pytch.when_green_flag_clicked
    def start(self):
        self.go_to_xy(0, -135)

        while not self.game_over_peluru and not self.win:
            pytch.create_clone_of(self)
            pytch.wait_seconds(0.7)

    @pytch.when_I_start_as_a_clone
    def start_clone(self):
        while not self.game_over_peluru and not self.win:
            self.change_y(3)

            if self.touching(Alien):
                self.hide()
                self.change_y(0)
                self.win = True
                pytch.broadcast("win")

    @pytch.when_key_pressed("ArrowLeft")
    def move_left(self):
        self.change_x(-move_size)

    @pytch.when_key_pressed("ArrowRight")
    def move_right(self):
        self.change_x(move_size)

    @pytch.when_I_receive("gameover")
    def stop_peluru(self):
        self.hide()
        self.game_over_peluru = True


class Rocket(pytch.Sprite):
    Costumes = ["rocket.png"]

    @pytch.when_green_flag_clicked
    def start(self):
        self.go_to_xy(0, -145)

    @pytch.when_key_pressed("ArrowLeft")
    def move_left(self):
        self.change_x(-move_size)

    @pytch.when_key_pressed("ArrowRight")
    def move_right(self):
        self.change_x(move_size)

    @pytch.when_I_receive("gameover")
    def stop_game(self):
        self.say_for_seconds("Game Over", 3)
        pytch.stop_all()

    @pytch.when_I_receive("win")
    def win_game(self):
        self.say_for_seconds("yeay, Win!", 3)
        pytch.stop_all()


class Alien(pytch.Sprite):
    Costumes = ["ufo.png"]
    speed = 0
    game_over = False
    win = False

    def select_level(self, level):
        if level == "easy":
            return random.randint(-2, -1)
        elif level == "medium":
            return random.randint(-4, -2)
        elif level == "hard":
            return random.randint(-6, -3)

    def drop(self, x, y):
        global score

        self.go_to_xy(x, y)
        speed = self.select_level(level)

        while self.y_position > -140 and not self.game_over and not self.win:
            self.change_y(speed)
            if self.touching(Rocket):
                pytch.broadcast("gameover")
                self.game_over = True

    @pytch.when_green_flag_clicked
    def set_position(self):
        while not self.game_over and not self.win:
            self.show()
            self.drop(random.randint(-145, 190), random.randint(120, 150))

    @pytch.when_I_receive("win")
    def win_game(self):
        self.hide()
        self.win = True


class Space(pytch.Stage):
    Backdrops = ["space.jpg"]
