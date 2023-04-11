from perlin_noise import PerlinNoise
from package.init import  *

init()
init2()

def genirateHeightMap(size):
    HeightMap = PerlinNoise(octaves=30, seed=4)

    xpix, ypix = size[0], size[1]

    pic = []

    for i in range(ypix):
        row = []
        for j in range(xpix):
            height = i / xpix
            width = j / ypix
            height_map = HeightMap([height, width])
            row.append(height_map)
            a = row.copy()
        pic.append(a)

    return pic

def realTimegenirateHeightMap(pos2, size, size2, world):
    HeightMap = PerlinNoise(octaves=30, seed=4)

    xpix, ypix = 800, 800

    pic = []

    pos = [0, 0]

    pos[0] = pos2[0]*1
    pos[1] = pos2[1]*1

    for i in range(int(pos[0]),int(pos[0]+size2[0])):
        row = []
        for j in range(int(pos[1]),int(pos[1]+size2[1])):
            #print(world.tiles[i][j]==0)
            if world.tiles[i][j]==0 or world.tiles[i][j]==255:
                height = i / xpix
                width = j / ypix
                height_map = HeightMap([height, width])
                row.append(height_map)
            else:
                row.append(255)
        a = row.copy()
        pic.append(a)

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
                self.tiles[x][y] = 0

    def genirate(self):
        hMap = genirateHeightMap([self.size[0], self.size[1]])




        #print(min(hMap), max(hMap))
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                var = (hMap[x][y] + 1) / 2 * 3

                if var < 3 and var > 2:

                    self.tiles[x][y] = Tile(2)
                elif var > 1.4:
                    self.tiles[x][y] = Tile(2)
                elif var < 1.4 and var > 1.2:
                    self.tiles[x][y] = Tile(3)
                else:
                    self.tiles[x][y] = Tile(1)
    def realTimeGenirate(self,pos, size):
        hMap = realTimegenirateHeightMap(pos,self.size,size, self)
        x2=0
        y2=0
        for x in range(pos[0],pos[0]+size[0]):
            x2 +=1
            for y in range(pos[1],pos[1]+size[1]):
                y2 += 1
                for i in range(size[0]):
                    try:

                        if hMap[x2+i][y2] == 255:
                            pass
                        else:
                            var = (hMap[x2+i][y2] + 1) / 2 * 3
                            if var < 3 and var > 2:
                                self.tiles[x+i][y] = Tile(2)
                            elif var > 1.4:
                                self.tiles[x+i][y] = Tile(2)
                            elif var < 1.4 and var > 1.2:
                                self.tiles[x+i][y] = Tile(3)
                            else:
                                self.tiles[x+i][y] = Tile(1)
                    except:
                        pass
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
                try:
                    window.blit(tilesId[self.tiles[x][y].id], [x * self.tileSize[0] - camera.pos[0], y * self.tileSize[1] - camera.pos[1]])
                except:
                    pass


