import pgzrun
from random import randint
from time import time

WIDTH=600
HEIGHT=600

start_time=0
total_time=0

totalsat=8

satillites=[]
for i in range(totalsat):
    sat=Actor("satillite")
    sat.pos=randint(50,550),randint(50,550)
    satillites.append(sat)


start_time=time()

def draw():
    screen.blit("space 3",(0,0))
    number=1
    for i in satillites:
        i.draw()
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+20))
        number+=1

def update():
    pass
 









pgzrun.go()