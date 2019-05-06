
import matplotlib.pyplot as plt
import random
import math
N = 2
dt = 0.01
t = 0
up = 10
down = 0
left = 0
right = 10


class Particle:
    def __init__(self, *args):
        if args == ():
            self.x = random.uniform(0, 10)
            self.vx = random.uniform(10, 100)
            self.y = random.uniform(0, 0)
            self.vy = random.uniform(0, 0)
            self.swap = False
        else :
            self.x, self.y, self.vx, self.vy = args

    def show(self):
        print("vx = ", self.vx)
        print("vy = ", self.vy, "\n")

    def calc(self):
        self.x += self.vx * dt
        self.y += self.vy * dt
        if abs(self.x - left) < 1 or abs(self.x - right) < 1:
            self.vx = -self.vx
        if abs(self.y - up) < 1 or abs(self.y - down) < 1:
            self.vy = -self.vy

    def __lt__(self, other):
        if self.x < other.x:
            return True
        return False


def sort_by_x(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j].x > arr[j + 1].x:
                arr[j].x, arr[j + 1].x = arr[j + 1].x, arr[j].x
    return arr
def sort_by_y(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j].y > arr[j + 1].y:
                arr[j].y, arr[j + 1].y = arr[j + 1].y, arr[j].y
    return arr


def collide_if_close(p1, p2):
    if math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) <= 0.5:
        print("До: ")
        p1.show()
        p2.show()
        if p1.x != p2.x:
            a = math.atan((p2.y - p1.y)/(p2.x - p1.x))  #Угол между линией центров и осьюю x
        else:
            a = 0
        vp1 = p1.vx * math.cos(a) + p1.vy * math.sin(a)  #Составляющие скорости, направленные вдоль линии центров. Они обмениваются значениями после столкновения
        vp2 = p2.vx * math.cos(a) + p2.vy * math.sin(a)
        vt1 = p1.vx * math.sin(a) + p1.vy * math.cos(a)  #Составляющие скорости, перпендикулярные линии центров. Они не меняются после столкновения
        vt2 = p2.vx * math.sin(a) + p2.vy * math.cos(a)

        vp1, vp2 = vp2, vp1 #Обмен значениями

        p1.vx = vp1*math.cos(a) - vt1*math.sin(a)
        p1.vy = vp1*math.sin(a) + vt1*math.cos(a)

        p2.vx = vp2*math.cos(a) - vt2*math.sin(a)
        p2.vy = vp2*math.sin(a) + vt2*math.cos(a)
        print("После: ")
        p1.show()
        p2.show()
        if abs(p1.vx) > 250 or abs(p1.vy)> 250:
            print("a = ", a)
            print("vp1 = ", vp2)
            print("vt1 = ", vt1)
            print("--------")
    return p1, p2



# p1 = Particle (1, 2, 3, 0)
# p2 = Particle (2, 2, 4, 0)
# p1, p2 = collide_if_close(p1, p2)
# print("---")
# p1.show()
# p2.show()




l = []
xValues = []
yValues = []
for i in range(N):
    p = Particle()
    l.append(p)
    xValues.append(p.x)
    yValues.append(p.y)



coll = list() #Временный массив для сортировки частиц и выявления тех, которые столкнутся
while t < 10000:
    for i in range(len(l)):
        l[i].swap = False
        l[i].calc()
        xValues[i] = l[i].x
        yValues[i] = l[i].y

    plt.cla()
    plt.xlim(left - 1, right + 1)
    plt.ylim(down - 1, up + 1)
    plt.scatter(xValues, yValues, s = 18)
    plt.pause(0.00000001)

    for i in range(len(l)):
        for j in range (len(l)):
            #print("i, j = ", i,", ", j)
            if i != j and (l[i].swap == False and l[j].swap == False):
                l[i], l[j] = collide_if_close(l[i], l[j])
                # l[i].swap = True
                # l[j].swap = True

    t += dt


    # coll = sort_by_x(l)
    # i = 0
    # while i < len(coll):
    #     if abs(coll[i].x - coll[i+1].x) > 0.1: #Удаляем элементы, отстоящие достаточно далеко друг от друга по x
    #         coll.pop([i])
    #         i -= 1
    #     i += 1

