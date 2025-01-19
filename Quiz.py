import pgzrun

TITLE="Quiz Master"
WIDTH = 870
HEIGHT = 650

questions=[]

currentQ=0
totalQ=0
smg=()



scrollerbox = Rect(0,0,870,80)
questionbox = Rect(20,100,650,150)
timerbox = Rect(700,100,150,150)
opt1= Rect(20,270,310,150)
opt2= Rect(340,270,310,150)
opt3= Rect(20,440,310,150)
opt4= Rect(340,440,310,150)
skipbox= Rect(700,270,150,320)
def draw():
    screen.fill("Black")
    screen.draw.filled_rect(scrollerbox,"orange")
    screen.draw.filled_rect(questionbox,"Green")
    screen.draw.filled_rect(timerbox,"orange")
    screen.draw.filled_rect(opt1,"green")
    screen.draw.filled_rect(opt2,"green")
    screen.draw.filled_rect(opt3,"green")
    screen.draw.filled_rect(opt4,"green")
    screen.draw.filled_rect(skipbox,"orange")
    smg=f"welcome to quizmaster. Q:{currentQ}:{totalQ}"
    screen.draw.textbox(smg,scrollerbox,color="white")
def update():
    scrollerbox.x-=2
    if scrollerbox.right<0:
        scrollerbox.x=870

def loadque():
    global totalQ
    with open("questions.txt","r") as file:
        for i in file:
            questions.append(i)
            totalQ +=1




loadque()
print (questions)
pgzrun.go()

