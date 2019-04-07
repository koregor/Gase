import numpy as np
import random
N = 1000


class Particle:
    def __init__(self):
        self.x = random.randrange(1, 10)
        self.vx = random.randrange(1, 10)

    def show(self):
        print(self.x)
        print(self.vx, "\n")


l = []
for i in range(N):
    l.append(Particle())
a = np.array(l)



# dt = 0.1
# t = 0
# wall_1 = 0
# wall_2 = 10
#
# a = np.zeros((100, 1), Particle)
# print (a)
#
# while t < 10:
#     p1.x += dt*p1.vx
#     if abs(p1.x - wall_1) < 0.1 or abs(p1.x - wall_2) < 0.1:
#         p1.vx = -p1.vx
#         print("boom")
#     t += dt
#     print(p1.x)
