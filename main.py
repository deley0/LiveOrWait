import pygame
from math import cos, sin, dist
from perlin_noise import PerlinNoise
import pygame.camera
from pygame.locals import *

from package.init import toInit

flags = FULLSCREEN | DOUBLEBUF

pygame.init()
clock = pygame.time.Clock()

resolution = [1920, 1080]

window = pygame.display.set_mode((0, 0), flags, 16)

pygame.display.set_caption('Live or wait')

keyControls = {"up": pygame.K_w, "down": pygame.K_s, "left": pygame.K_a, "right": pygame.K_d}  # Управление

pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])

tileTexture1 = pygame.transform.scale(pygame.image.load("res\\texture\\water.png"), (16 * 4, 16 * 4)).convert()
tileTexture2 = pygame.transform.scale(pygame.image.load("res\\texture\\grass.png"), (16 * 4, 16 * 4)).convert()
tileTexture3 = pygame.transform.scale(pygame.image.load("res\\texture\\sand.png"), (16 * 4, 16 * 4)).convert()

tilesId = {
    1: tileTexture1,
    2: tileTexture2,
    3: tileTexture3,
}

from package.entitys import *


player = Player([0, 0], pygame.image.load("res\\texture\\Player_image.png"), keyControls)


class Tile:
    def __init__(self, id):
        self.id = id


toInit(player, Tile, tilesId, resolution)

from package.map import genirateHeightMap, Camera, World

class SolidObj:
    def __init__(self, pos, size):
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.collided = False

    def collaid(self, entity):
        rect = pygame.Rect(entity.pos[0], entity.pos[1], entity.texture.get_size()[0], entity.texture.get_size()[1])

        if self.rect.colliderect(rect):
            self.collided = True
        else:
            self.collided = False

    def draw(self, window):
        if self.collided:
            pygame.draw.rect(window, (0, 200, 0), self.rect)
        else:
            pygame.draw.rect(window, (200, 0, 0), self.rect)


class Button:
    pass


wall = SolidObj([0, 0], [100, 100])

run = True
map = World([500, 500])
map.genirate()
cam = Camera()
t = 0

while run:

    t += 1
    cam.update()
    window.fill((255, 255, 255))

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

    player.control(keys)
    player.on()
    map.draw(window, cam)
    player.draw(window, cam)

    pygame.display.update()

    wall.collaid(player)

    # Измеряем FPS
    fps = int(clock.get_fps())
    if t % 100 == 0:
        print("FPS:", fps)

    # Ограничиваем FPS до 60
    clock.tick(6000)
