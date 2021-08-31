import random

class Map:
    def __init__(self, fname):
        self.map = []
        with open(fname) as f:
            self.n, self.m = map(int, f.readline().split())
            for _ in range(self.n):
                self.map.append([0 if k == '0' else 1 for k in f.readline() if k == '0' or k == '1'])

    def move(self, x, y, d):
        dxy = ( (0, 1), (1, 0), (0, -1), (-1, 0) )
        nx, ny = x + dxy[d][0], y + dxy[d][1]
        if nx < 0 or nx >= self.m: return (x, y)
        if ny < 0 or ny >= self.n: return (x, y)
        if self.map[ny][nx] == 1: return (x, y)
        return (nx, ny)

errlimit = 0.0001
mapName = input("Map Name : ")
env = Map(mapName)
mat = [ [0]*env.m for _ in range(env.n) ]
for _ in range(1000):
    errmax = 0
    for y in range(env.n):
        for x in range(env.m):
            if env.map[y][x] == 1: continue
            if y==env.n-1 and x==env.m-1: continue
            t = 0
            for d in range(4):
                nx, ny = env.move(x, y, d)
                t += (-1+mat[ny][nx])*0.25
            if abs(mat[y][x]-t) > errmax: errmax = abs(mat[y][x]-t)
            mat[y][x] = t
    if errmax <= errlimit: break

for y in range(env.n):
    for x in range(env.m):
        if env.map[y][x] == 1: mat[y][x] = "X"
        else: mat[y][x] = "%.1f"%mat[y][x]

fmt = "{:^9}"*env.m
for i in range(env.n):
    print(fmt.format(*mat[i]))
