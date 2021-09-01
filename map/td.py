import random

alpha = 0.01

class Map:
    def __init__(self, fname):
        self.map = []
        with open(fname) as f:
            self.n, self.m = map(int, f.readline().split())
            for _ in range(self.n):
                self.map.append([0 if k == '0' else 1 for k in f.readline() if k == '0' or k == '1'])
        self.mat = [ [0]*self.m for _ in range(self.n) ]

    def move(self, x, y, d):
        dxy = ( (0, 1), (1, 0), (0, -1), (-1, 0) )
        nx, ny = x + dxy[d][0], y + dxy[d][1]
        if nx < 0 or nx >= self.m: nx = x
        elif ny < 0 or ny >= self.n: ny = y
        elif self.map[ny][nx] == 1: nx, ny = x, y
        self.mat[y][x] = (1-alpha)*self.mat[y][x] + alpha*(-1+self.mat[ny][nx])
        return (nx, ny)

    def moveToEnd(self):
        x, y = 0, 0
        while x != self.m-1 or y != self.n-1:
            x, y = self.move(x, y, random.randrange(4))

    def getTable(self):
        tbl = []
        for y in range(env.n):
            tbl.append(["X" if self.map[y][x] == 1 else f"{self.mat[y][x]:.1f}" for x in range(self.m)])
        return tbl

mapName = input("Map Name : ")
env = Map(mapName)
k = int(input("Iteration count : "))
for it in range(k):
    env.moveToEnd()

    if it%(k//10) == (k//10)-1:
        print(f"Iteration : {it+1}/{k}")
        tbl = env.getTable()
        fmt = "{:^9}"*env.m
        for i in range(env.n):
            print(fmt.format(*tbl[i]))
