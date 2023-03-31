from perlin_noise import PerlinNoise
from package.init import  *

init()


def genirateHeightMap(size):
    HeightMap = PerlinNoise(octaves=30, seed=3)

    xpix, ypix = size[0], size[1]
    pic = [[HeightMap([i / xpix, j / ypix]) for j in range(xpix)] for i in range(ypix)]

    return pic


class Camera:
    def __init__(self):
        self.pos = [0, 0]

    def update(self):
        self.pos[0] += (player.pos[0] - self.pos[0] - resolution[0] / 2) / 10
        self.pos[1] += (player.pos[1] - self.pos[1] - resolution[1] / 2) / 10


class World:
    def __init__(self, size):
        self.tiles = []
        self.size = size
        self.tileSize = [64, 64]
        for x in range(size[0]):
            self.tiles.append([0] * size[1])

        for x in range(size[0]):
            for y in range(size[1]):
                self.tiles[x][y] = Tile(1)

    def genirate(self):
        hMap = genirateHeightMap([self.size[0], self.size[1]])
        print(min(hMap), max(hMap))
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                var = (hMap[x][y] + 1) / 2 * 3

                if var < 3 and var > 2:

                    self.tiles[x][y].id = 2
                elif var > 1.4:
                    self.tiles[x][y].id = 2
                elif var < 1.4 and var > 1.2:
                    self.tiles[x][y].id = 3
                else:
                    self.tiles[x][y].id = 1

    def draw(self, window, camera):
        cameraTilePos = [int(camera.pos[0] / self.tileSize[0]), int(camera.pos[1] / self.tileSize[1])]
        cameraTileSize = [int(resolution[0] / self.tileSize[0]) + 1, int(resolution[1] / self.tileSize[1]) + 2]

        if cameraTilePos[0] + cameraTileSize[0] > self.size[0]:
            cameraTilePos[0] = self.size[0] - cameraTileSize[0]

        if cameraTilePos[1] + cameraTileSize[1] > self.size[1]:
            cameraTilePos[1] = self.size[1] - cameraTileSize[1]

        if cameraTilePos[0] < 0:
            cameraTilePos[0] = 0

        if cameraTilePos[1] < 0:
            cameraTilePos[1] = 0

        for x in range(cameraTilePos[0], cameraTilePos[0] + cameraTileSize[0]):
            for y in range(cameraTilePos[1], cameraTilePos[1] + cameraTileSize[1]):
                window.blit(tilesId[self.tiles[x][y].id],
                            [x * self.tileSize[0] - camera.pos[0], y * self.tileSize[1] - camera.pos[1]])



