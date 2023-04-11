import pygame
from math import cos, sin, dist
from perlin_noise import PerlinNoise
import pygame.camera
from pygame.locals import *

from package.init import toInit
import random


# Arguments:
#display: the surface to draw to
#position: the position of the effect onscreen
#size: the size of the effect (normally



flags = FULLSCREEN | DOUBLEBUF
flags2 = pygame.HWSURFACE | pygame.OPENGL | pygame.DOUBLEBUF

#window = pygame.display.set_mode((600, 600), flags2)

pygame.init()
clock = pygame.time.Clock()

resolution = [1920, 1080]

window = pygame.display.set_mode((0, 0), flags, 16)



pygame.display.set_caption('Live or wait')

keyControls = {"up": pygame.K_w, "down": pygame.K_s, "left": pygame.K_a, "right": pygame.K_d, "drop": pygame.K_q, "use": pygame.K_z}  # Управление

pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])

tileTexture1 = pygame.transform.scale(pygame.image.load("res\\texture\\water.png"), (16 * 4, 16 * 4)).convert()
tileTexture2 = pygame.transform.scale(pygame.image.load("res\\texture\\grass.png"), (16 * 4, 16 * 4)).convert()
tileTexture3 = pygame.transform.scale(pygame.image.load("res\\texture\\sand.png"), (16 * 4, 16 * 4)).convert()

tilesId = {
    1: tileTexture1,
    2: tileTexture2,
    3: tileTexture3,
}











class Tile:
    def __init__(self, id):
        self.id = id

solid_objs = []

toInit( Tile, tilesId, resolution, solid_objs)
from package.entitys import *
items = []

toInit3(items)
from package.player import Player
player = Player([0, 0], pygame.image.load("res\\texture\\Player_image.png"), keyControls)
toInit2(player, keyControls)
from package.map import *
cam = Camera()


class SolidObj:
    def __init__(self, pos, size):
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.collided = False
        self.size = size
        self.id = 0

    def check_collision(self, player):
        player_rect = pygame.Rect(player.pos[0], player.pos[1], player.texture.get_size()[0], player.texture.get_size()[1])
        if self.rect.colliderect(player_rect):
            self.collided = True
        else:
            self.collided = False

        return self.collided

    def draw(self, window):
        newRect = pygame.Rect(self.rect.x-cam.pos[0], self.rect.y-cam.pos[1], self.size[0], self.size[1])
        if self.collided:
            pygame.draw.rect(window, (0, 200, 0), newRect)
        else:
            pygame.draw.rect(window, (200, 0, 0), newRect)


class Button:
    pass


solid_objs.append(SolidObj([0, 0], [100, 100]))
solid_objs.append(SolidObj([0, 100+100*1], [100, 100]))
solid_objs.append(SolidObj([0, 200+100*2], [100, 100]))
solid_objs.append(SolidObj([0, 300+100*3], [100, 100]))

run = True
map = World((1000, 1000))
#map.genirate()
dioWin = diologWin("Делаю диалоговое окно, ПОЧТИ сделал...", keyControls)
t = 0



while run:
    if t%2==0:
        map.realTimeGenirate([round((player.pos[0]-64*16.5)/64),round((player.pos[1]-64*10)/64)], [33, 20])
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

    for i in range(4):
        solid_objs[i].draw(window)

    player.colid()
    var1 = 0
    for i in range(len(items)):
        try:
            items[i].on()
        except:
            break
    for i in range(len(items)):

        items[i].draw(window, cam)
        items[i].colid()

    player.draw(window, cam)
    dioWin.update()
    dioWin.draw(window)
    dioWin.on(keys)


    pygame.display.flip()



    # Измеряем FPS
    fps = int(clock.get_fps())
    if t % 100 == 0:
        print("FPS:", fps)


    # Ограничиваем FPS до 60
    clock.tick(60)
