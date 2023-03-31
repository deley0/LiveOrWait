

class Entity:

    def __init__(self, pos, hp, image):
        self.pos = pos
        self.hp = hp
        self.isLive = True
        self.texture = image

    def on(self):
        if self.hp < 0:
            self.isLive = False

    def draw(self, window, camera):
        window.blit(self.texture, [self.pos[0]-camera.pos[0],self.pos[1]-camera.pos[1]])





class Player(Entity):

    def __init__(self, pos, image, keyControls):
        super().__init__(pos, 100, image)
        self.velocity = [0,0]
        self.invent = [[0] * 50] * 30
        self.speed = 1.5
        self.keyControls = keyControls

    def on(self):
        super().on()
        self.velocity[0] /= 1.11
        self.velocity[1] /= 1.11
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]

    def draw(self, window, camera):
        super().draw(window, camera)

    def control(self, keys):
        if keys[self.keyControls["left"]]:
            self.velocity[0] -= self.speed
        if keys[self.keyControls["right"]]:
            self.velocity[0] += self.speed
        if keys[self.keyControls["up"]]:
            self.velocity[1] -= self.speed
        if keys[self.keyControls["down"]]:
            self.velocity[1] += self.speed