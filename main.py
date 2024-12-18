import pygame as pg
from object import Object
from world import World
from camera import Camera
from threading import Thread
from client import client


pg.init()

# client.plr_name = input("your name: ")

class Game:
    def __init__(self) -> None:
        self.screen = pg.display.set_mode((1000, 600))
        self.screen_h, self.screen_w = self.screen.get_height(), self.screen.get_width()
        self.world = World()
        self.camera = Camera(self.screen_w, self.screen_h)


        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.post_cd = 0


        # todo start functions
        self.world.generate_word()
        # client.send_plr_join()
        pg.mouse.set_visible(False)


    def update(self):
        if self.delta_time == 0:
            self.delta_time = 1

        self.world.faces, self.world.points = self.camera.camera_view(self.world.objects, self.screen_w, self.screen_h)
        self.camera.controls(self.screen_w, self.screen_h, self.world.objects, self.delta_time)
        self.camera.collisions(self.world.objects, self.delta_time)
        # try:
        #     if self.post_cd >= 2:
        #         client.send_pos(self.camera.x, self.camera.y, self.camera.z)
        #         self.post_cd = 0
        #     self.post_cd += 1 / self.delta_time
        # except Exception:
        #     pass

    def draw(self):
        self.world.draw(self.screen, self.camera, self.screen_w, self.screen_h)


    def run(self):
        while True:
            self.screen.fill("black")
            self.update()
            self.draw()

            for e in pg.event.get():
                if e.type == pg.QUIT:
                    quit()

            pg.display.flip()
            self.clock.tick(0)
            pg.display.set_caption(str(self.clock.get_fps()))
            self.delta_time = self.clock.get_fps() / 60


if __name__ == "__main__":
    game = Game()
    game.run()