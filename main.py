import numpy as np
import random
N = 10000
dt = 0.1
t = 0
wall_1 = 0
wall_2 = 10


class Particle:
    def __init__(self):
        self.x = random.randrange(1, 10)
        self.vx = random.randrange(-10, 10)

    def show(self):
        print("x = ", self.x)
        print("vx = ", self.vx, "\n")

    def calc(self):
        self.x += self.vx * dt
        if abs(self.x - wall_1) < 0.1 or abs(self.x - wall_2) < 0.1:
            self.vx = -self.vx

    def __lt__(self, other):
        if self.x < other.x:
            return True
        return False

    def __gt__(self, other):
        if self.x > other.x:
            return True
        return False


def collide_if_close(p1, p2):
    if abs(p1.x - p2.x) < 0.1:
        tmp = p1.vx
        p1.vx = p2.vx
        p2.vx = tmp
    return p1, p2



l = []
for i in range(N):
    l.append(Particle())
a = np.array(l)

while t < 100:
    for i in a:
        i.calc()
    a = np.sort(a)
    for i in range(len(a) - 1):
        a[i], a[i+1] = collide_if_close(a[i], a[i+1])

    t += dt
    print("-------------------")




