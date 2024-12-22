import pgzrun
from random import randint
from time import time

WIDTH=600
HEIGHT=600

start_time=0
total_time=0

totalsat=8
currentsat=0
satillites=[]
lines=[]
for i in range(totalsat):
    sat=Actor("satillite")
    sat.pos=randint(50,550),randint(50,550)
    satillites.append(sat)


start_time=time()

def draw():
    global total_time
    screen.blit("space 3",(0,0))
    if currentsat < totalsat:
        total_time=round(time()-start_time)
        screen.draw.text (str(total_time),(25,25),fontsize=30)
    else:
        screen.draw.text (str(total_time),(25,25),fontsize=30)
    number=1
    for i in satillites:
        i.draw()
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+20))
        number+=1
    for i in lines:
        screen.draw.line(i[0],i[1],"white")

def update():
    pass
def on_mouse_down(pos):
 global currentsat,totalsat,lines
 if currentsat < totalsat:
     if satillites[currentsat].collidepoint(pos):
         if currentsat:
             lines.append ((satillites[currentsat-1].pos,satillites[currentsat].pos))
         currentsat+=1
     else:
         lines=[]
         currentsat=0
         

 









pgzrun.go()