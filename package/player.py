from package.entitys import Entity
from package.items import Item
from package.init import *
import pygame
init3()

class Player(Entity):

    def __init__(self, pos, image, keyControls):
        super().__init__(pos, 100, image)

        self.invent = [[0] * 50] * 30

        self.keyControls = keyControls


    def colid(self):
        super().colid()



    def on(self):
        super().on()



    def draw(self, window, camera):
        super().draw(window, camera)

    def control(self, keys):
        #for obj in solid_objs:
        #    if obj.check_collision(self):
        #        self.velocity = [0, 0]
        if keys[self.keyControls["left"]]:
            self.velocity[0] -= self.speed
        if keys[self.keyControls["right"]]:
            self.velocity[0] += self.speed
        if keys[self.keyControls["up"]]:
            self.velocity[1] -= self.speed
        if keys[self.keyControls["down"]]:
            self.velocity[1] += self.speed
        if keys[self.keyControls["drop"]]:
            items.append(Item([self.pos[0], self.pos[1]], 100, pygame.image.load("res\\texture\\money.png").convert(), 1))
            items[len(items) - 1].colisRad = 17
            items[len(items) - 1].velocity[0] = self.velocity[0] * 3
            items[len(items) - 1].velocity[1] = self.velocity[1] * 3