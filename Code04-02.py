
import turtle
import random

## 전역 변수 선언 부분 ##
swidth, sheight, pSize, exitCount = 300, 300, 3, 0
#윈도우 폭, 윈도우 높이, 펜의 두께, 윈도창 밖으로 빠져나간 횟수를 위해 준비
r, g, b, angle, dist, curX, curY = [0] * 7
#색상(R), 색상(G), 색상(B), 임의로 이동할 각도, 임의로 이동할 거리, 거북이의 위치(X), 거북이의 위치(Y)

##메인 코드 부분 ##
turtle.title("거북이가 맘대로 다니기")
turtle.shape("turtle")
turtle.pensize(pSize)
turtle.setup(width = swidth + 30, height = sheight + 30)
turtle.screensize(swidth, sheight)

while True :
    r = random.random()
    b = random.random()
    b = random.random()
    turtle.pencolor((r, g, b))

    angle = random.randrange(0, 360)
    dist = random.randrange(1, 100)
    turtle.left(angle)
    turtle.forward(dist)
    curX = turtle.xcor()
    curY = turtle.ycor()

    if (-swidth / 2 <= curX and curY <= swidth / 2) and (-sheight / 2 <= curY and curY <= sheight / 2) :
        pass
    else :
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()

        exitCount += 1
        if exitCount >= 5:
            break

turtle.done()
