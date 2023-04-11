from package.entitys import Entity
import random
from package.init import *
from math import *

class Item(Entity):
    def __init__(self, pos, hp, image, id):
        super().__init__(pos, hp, image)
        self.id = id
        self.num = 1

    def on(self):
        super().on()
        if random.randint(1,2) == 1:
            rand = random.randint(0,len(items)-1)
            if dist(items[rand].pos, self.pos)<50 and not self is items[rand]:
                self.num += items[rand].num
                items.pop(rand)


    def colid(self):
        super().colid()

    def draw(self, window, camera):
        super().draw(window, camera)