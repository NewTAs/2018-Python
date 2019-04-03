import turtle    #turtle 함수를 불러온다
import random    #random 함수를 불러온다

##함수 선언 부분##
def slc(x, y) :    #slc 함수 선언
    global r, g, b    #r, g, b를 전역 변수(모든 부분에서 사용 가능)로 선언
    turtle.pencolor((r, g, b))    #거북이 흔적의 색깔을 r, g, b 혼합색으로 설정
    turtle.pendown()    #거북이의 흔적 보여줌으로 설정
    turtle.goto(x, y)    #거북이가 x, y 좌표로 이동

def src(x, y) :    #src 함수 선언
    turtle.penup()    #거북이의 흔적을 보여주지 않음으로 설정
    turtle.goto(x, y)    #거북이가 x, y 좌표로 이동

def smc(x, y) :
    global r, g, b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()

##변수 선언 부분##
pSize = 10
r, g, b = [0] * 3

##메인 코드 부분##
turtle.title("거북이로 그림 그리기")
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(slc, 1)
turtle.onscreenclick(smc, 2)
turtle.onscreenclick(src, 3)

turtle.done()
