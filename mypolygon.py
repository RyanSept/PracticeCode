from swampy.TurtleWorld import *
import random,math
world = TurtleWorld()
bob = Turtle()
jay=Turtle()
print bob
def randmov(t):
    for i in range(200):
        x=random.randint(1,100)
        y=random.randint(1,180)
        if i%2==0 and i%3==0 and i%4==0:
            rt(t,270)
            fd(t,x)
            pu(t)
            pd(t)
        if i%2!=0 and i%3!=0 and i%4!=0:
            lt(t,270)
            fd(t,y)
            pu(t)
            pd(t)

def sq(t,length):
    fd(t,length)
    lt(t)
    fd(t,length)
    lt(t)
    fd(t,length)
    lt(t)
    fd(t,length)
def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)
def polygon(t, n, length):
    angle = 360.0 / n
    for i in range(n):
        fd(t, length)
        lt(t, angle)
bob.delay=0.05
##polygon(bob,14,50)
##sq(bob,50)
jay.delay=0.01
circle(jay,70)
randmov(bob), randmov(jay)

wait_for_user()
