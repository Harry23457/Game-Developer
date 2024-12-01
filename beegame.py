import pgzrun
from random import randint

WIDTH=500
HEIGHT=500

score=0

gameover=False
bee=Actor("bee")
bee.pos=(50,50)
flower=Actor("bee flower")
flower.pos=(250,100)

def draw():
    screen.blit("bee backdrop",(0,0))
    flower.draw()
    bee.draw()
    screen.draw.text("score:"+str(score),color=("black"),topleft=(50,50))
    if gameover==True:
        screen.fill("yellow")
        screen.draw.text("Times up your score is"+str(score),color=("black"),center=(250,250))


def update():
    if keyboard.up:
        bee.y-=5
    if keyboard.left:
        bee.x-=5
    if keyboard.down:
        bee.y+=5
    if keyboard.right:
        bee.x+=5

pgzrun.go()