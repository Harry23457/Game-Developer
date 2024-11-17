from random import randint 
import pgzrun
import time

WIDTH = 600
HEIGHT = 600

score=0

message=""
image = Actor("ant")


image.pos=randint(50,450),randint(50,450)
def draw():
    screen.fill("light blue")
    image.draw()
    screen.draw.text(message,center=(400,50))
    screen.draw.text("score:"+ str(score),center=(50,50))
def on_mouse_down(pos):
    global message,score
    if image.collidepoint(pos):
        message="Nice Shot"
        score+=1 
    else:
        message="Missed"
def update():
    image.pos=randint(50,450),randint(50,450)
    time.sleep(0.5)
    

pgzrun.go()