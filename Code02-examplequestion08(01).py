import turtle    #turtle 함수를 불러온다
import random    #random 함수를 불러온다

##함수 선언 부분##
def slc(x, y) :    #slc함수를 선언
    global r, g, b    #r, g, b를 전체 선언
    r = random.random()    #r을 랜덤으로 선언
    g = random.random()    #g를 랜덤으로 선언
    b = random.random()    #b를 랜덤으로 선언

    turtle.title("Code02-연습문제08")    #거북이 프로그램의 이름 설정
    turtle.shape("turtle")    #거북이의 모양 설정

    turtle.color((r, g, b))    #거북이의 색깔을 설정(r, g, b 혼합)
    turtle.penup()    #거북이의 흔적을 안남기게 설정

    tSize = random.randrange(1, 10)    #tSize를 1~9까지의 숫자를 랜덤으로 돌린 후, 선언
    turtle.turtlesize(tSize)    #거북이의 크기를 tSize로 설정

    tSpin = random.randrange(0, 360)    #tSpin을 0~359까지의 숫자를 랜덤으로 돌린 후, 선언
    turtle.right(tSpin)    #거북이를 오른쪽으로 tSpin만큼 회전
    
    turtle.stamp()    #거북이의 위치에서 도장을 찍음
    turtle.goto(x, y)    #거북이가 x, y좌표로 이동

##메인 코드 부분##
turtle.onscreenclick(slc, 1)    #마우스 왼쪽 클릭 시, slc 함수 실행
