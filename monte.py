import random

class Map:
	def __init__(self, fname):
		self.map = []
		with open(fname) as f:
			self.n, self.m = map(int, f.readline().split())
			for _ in range(self.n):
				self.map.append([0 if k == '0' else 1 for k in f.readline()])

	def move(self, x, y, d):
		dxy = ( (0, 1), (1, 0), (0, -1), (-1, 0) )
		nx, ny = x + dxy[d][0], y + dxy[d][1]
		if nx < 0 or nx >= self.m: return (x, y)
		if ny < 0 or ny >= self.n: return (x, y)
		if self.map[ny][nx] == 1: return (x, y)
		return (nx, ny)

	def moveToEnd(self):
		x, y = 0, 0
		history = []
		while x != self.m-1 or y != self.n-1:
			x, y = self.move(x, y, random.randrange(4))
			history.append((x, y))
		return history

mapName = input("Map Name : ")
env = Map(mapName)
print(env.moveToEnd())
