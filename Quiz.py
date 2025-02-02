import pgzrun

TITLE="Quiz Master"
WIDTH = 870
HEIGHT = 650

questions=[]

score = 0
currentQ=0
totalQ=0
smg=()
timeq=15
finished=False

scrollerbox = Rect(0,0,870,80)
questionbox = Rect(20,100,650,150)
timerbox = Rect(700,100,150,150)
opt1= Rect(20,270,310,150)
opt2= Rect(340,270,310,150)
opt3= Rect(20,440,310,150)
opt4= Rect(340,440,310,150)
optlist= [opt1,opt2,opt3,opt4]
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
    screen.draw.textbox(str(timeq),timerbox,color="white")
    screen.draw.textbox(q[0].strip(),questionbox,color="white")
    screen.draw.textbox("skip",skipbox,color = "white",angle = -90)
    index=1
    for i in optlist:
        screen.draw.textbox(q[index].strip(),i,color ="white")
        index += 1

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

def nextque():
    global currentQ
    currentQ += 1
    return questions.pop(0).split("|")

def on_mouse_down(pos):
    index=1
    for i in optlist:
        if i.collidepoint(pos):
            if index is int(q[5]):
                correctanwser()
            else:
                gameover()

        index+=1

def correctanwser():
    global timeq, score, q
    score += 1
    if questions:
        q=nextque()
        timeq=15
    else :
        gameover()



def gameover():
    global timeq, finished, q, score
    message=f"game over you got {score} questions correct"

    q=[message,"-","-","-","-",0]
    timeq=0
    finished=True

def timer():
    global timeq
    if timeq:
        timeq = timeq - 1
    else:
        gameover()
 


clock.schedule_interval(timer,1)
loadque()
q=nextque()
print (questions[0])
pgzrun.go()

