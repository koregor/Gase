import numpy as np
import matplotlib.pyplot as plt
import random
import time
N = 100
dt = 0.01
t = 0
wall_1 = 0
wall_2 = 10
wall_3 = 1
wall_4 = -1


class Particle:
    def __init__(self):
        self.x = random.uniform(-10, 10)
        self.vx = random.uniform(-100, 100)
        self.y = random.uniform(-2, 2)
        self.vy = random.uniform(-100, 100)




    def show(self):
        print("x = ", self.x)
        print("vx = ", self.vx, "\n")

    def calc(self):
        self.x += self.vx * dt
        self.y += self.vy * dt
        if abs(self.x - wall_1) < 1 or abs(self.x - wall_2) < 1:
            self.vx = -self.vx
        if abs(self.y - wall_3) < 0.1 or abs(self.y - wall_4) < 0.1:
            self.vy = -self.vy

    def __lt__(self, other):
        if self.x < other.x:
            return True
        return False


def collide_if_close(p1, p2):
    if abs(p1.x - p2.x) < 0.1:
        tmp = p1.vx
        p1.vx = p2.vx
        p2.vx = tmp
    elif abs(p1.y - p2.y) < 0.1:
        tmp1 = p1.vy
        p1.vy = p2.vy
        p2.vy = tmp1
    return p1, p2

l = []
xValues = []
yValues = []
c = []
for i in range(N):
    p = Particle()
    l.append(p)
    xValues.append(p.x)
    yValues.append(p.y)

plt.xlim((wall_1, wall_2))


while t < 10:
    for i in range(len(l) - 1):
        l[i].calc()
        xValues[i] = l[i].x
        yValues[i] = l[i].y



    plt.cla()
    plt.scatter(xValues, yValues, s=1)
    plt.axis([-10, 10 ,-2 ,2])
    plt.pause(0.019)
    t += dt

    # l = np.sort(l)
    # for i in range(len(l) - 1):
    #     l[i], l[i+1] = collide_if_close(l[i], l[i+1])


