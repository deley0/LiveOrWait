import pygame


from package.init import *
from math import *

init()
init2()

class Entity:

    def __init__(self, pos, hp, image):
        self.pos = pos
        self.hp = hp
        self.isLive = True
        self.texture = image
        self.size = [64,64]
        self.speed = 1.5
        self.velocity = [0, 0]
        self.colisRad = 35

    def on(self):
        if self.hp < 0:
            self.isLive = False
        self.velocity[0] /= 1.11
        self.velocity[1] /= 1.11
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]

    def colid(self):
        playerSpeed = dist([0, 0], [self.velocity[0], self.velocity[1]])
        if playerSpeed>0:
            for obj in solid_objs:

                if obj.check_collision(self):
                    if obj.id == 1:
                        objCX = obj.rect.x + obj.rect.size[0] / 2
                        objCY = obj.rect.y + obj.rect.size[1] / 2
                        dy = objCY - (self.pos[1] + self.size[1] / 2)
                        dx = objCX - (self.pos[0] + self.size[0] / 2)
                        self.pos = [self.pos[0] - cos(atan2(dy, dx)) * 3, self.pos[1] - sin(atan2(dy, dx)) * 3]
                        self.velocity = [self.velocity[0] / 1.1, self.velocity[1] / 1.1]
                if obj.id == 0:
                    points = []
                    playerCx = self.pos[0] + self.size[0] / 2
                    playerCy = self.pos[1] + self.size[1] / 2
                    step = (pi * 2) / 20

                    num = 0
                    for i in range(20):
                        points.append(pygame.Rect([playerCx + cos(i * step) * self.colisRad, playerCy + sin(i * step) * self.colisRad, 1, 1]))
                        if points[i].colliderect(obj.rect):
                            num += 1

                            self.pos[0] -= cos(i * step) * playerSpeed / (num + 1)
                            self.pos[1] -= sin(i * step) * playerSpeed / (num + 1)
                            self.velocity[0] /= 4
                            self.velocity[1] /= 4

    def draw(self, window, camera):
        window.blit(self.texture, [self.pos[0] - camera.pos[0], self.pos[1] - camera.pos[1]])

class diologWin:
    def __init__(self, text, keyControls):
        self.keyControls = keyControls
        self.text = text
        self.font = pygame.font.SysFont('Arial', 30)
        self.rect = pygame.Rect(0, 0, 1920, 300)
        self.text_surfaces=[]
        self.text_surfaces.append(self.font.render(self.text, True, (250, 250, 250)))
        self.text_surfaces.append(self.font.render(self.text, True, (250, 250, 250)))
        self.text_surfaces.append(self.font.render(self.text, True, (250, 250, 250)))
        self.text_surfaces.append(self.font.render(self.text, True, (250, 250, 250)))

        self.selectFile = "res\\dialogues\\test.txt"


        self.anim = True
        self.t = 0
        self.idList = ["name1", "name2"]
        self.selectTag = self.idList[0]

        self.score = 0
        self.isUpdate = False
    def draw(self, window):
        pygame.draw.rect(window, (20, 20, 20), self.rect)
        pygame.draw.rect(window, (250, 250, 250), self.rect, 20)
        window.blit(self.text_surfaces[0], (50, 50))
        window.blit(self.text_surfaces[1], (50, 100))
        window.blit(self.text_surfaces[2], (50, 150))
        window.blit(self.text_surfaces[3], (50, 200))

    def on(self, keys):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == self.keyControls["use"]:

                self.score += 1
                self.selectTag = self.idList[self.score]

    def update(self):
        flag = False

        for i in range(4):

            self.text_surfaces[i] = self.font.render("", True, (250, 250, 250))
        with open(self.selectFile,"r", encoding='utf-8') as f:
            lines = f.readlines()
            for i in range(len(lines)):
                if "\>"in lines[i]:
                    if self.selectTag in lines[i]:
                        for i2 in range(6):
                            if "\<"in lines[i-i2]:



                                for i3 in range(i-(i-i2)-1):
                                    if "\>" in lines[i - i2+i3+1]:
                                        flag = True
                                        break
                                    self.text_surfaces[i3] = self.font.render(lines[i - i2+i3+1][:-1], True, (250, 250, 250))
                                    if i3 == 3:
                                        flag = True
                                        break
                                if flag:
                                    break
                            if flag:
                                break
                        if flag:
                            break
                    if flag:
                        break
                if flag:
                    break













