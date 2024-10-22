import pytch


class Raka(pytch.Sprite):
    Costumes = ["Dani.png"]
    speed = 1

    @pytch.when_green_flag_clicked
    def start(self):
        self.go_to_xy(210, -80)

    @pytch.when_I_receive("jalan")
    def jalan(self):
        self.change_x(-self.speed)

    @pytch.when_I_receive("ketabrak")
    def ketabrak(self):
        self.speed = 0

        for i in range(0, 15):
            self.change_x(-8)
            self.change_y(5)
            self.turn_degrees(-35)
            self.say("aaaaaa")
            pytch.wait_seconds(0.1)
        for i in range(0, 20):
            self.change_x(-8)
            self.change_y(-5)
            self.turn_degrees(-35)
            self.say("aaaaaa")
            pytch.wait_seconds(0.1)

        self.say("Aw, sakit!")


class Truck(pytch.Sprite):
    Costumes = ["truck.png"]
    speed = 1
    ketabrak = False

    @pytch.when_green_flag_clicked
    def start(self):
        self.go_to_xy(150, -120)

        while not self.ketabrak:
            if pytch.key_pressed(" "):
                self.change_x(-self.speed)
                pytch.broadcast("jalan")

            if self.touching(Halangan):
                self.speed = 0
                self.say("Aduh Ketabrak")
                pytch.broadcast("ketabrak")
                self.ketabrak = True


class Halangan(pytch.Sprite):
    Costumes = ["log1.png"]

    @pytch.when_green_flag_clicked
    def start(self):
        # self.turn_degrees(90)
        self.go_to_xy(-100, -120)


class GreenField(pytch.Stage):
    Backdrops = ["green-field.jpg"]
