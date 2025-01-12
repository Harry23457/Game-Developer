import pgzrun

TITLE="Quiz Master"
WIDTH = 870
HEIGHT = 650

scrollerbox = Rect(0,0,870,80)
questionbox = Rect(20,100,650,150)
timerbox = Rect(700,100,150,150)
def draw():
    screen.fill("Black")
    screen.draw.filled_rect(scrollerbox,"orange")
    screen.draw.filled_rect(questionbox,"Green")
    screen.draw.filled_rect(timerbox,"orange")


def update():
    pass




pgzrun.go()

