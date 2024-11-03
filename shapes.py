import pgzrun
import random

WIDTH = 300
HEIGHT = 300

def draw():
    w=300
    h=100
    c1=random.randint(0,255)
    c2=random.randint(0,255)
    c3=random.randint(0,255)
    screen.fill("white")
    screen.draw.filled_circle((150,150),60,(c1,c2,c3))
    screen.draw.line((0,0),(300,300),(c1,c2,c3))
    for i in range(10):
        c1=random.randint(0,255)
        c2=random.randint(0,255)
        c3=random.randint(0,255)
        obj = Rect(0,0,w,h)
        obj.center=150,150
        screen.draw.rect(obj,(c1,c2,c3))
        w-=10
        h+=10


pgzrun.go()