import turtle    #turtle함수를 불러온다

##함수 선언 부분##

##변수 선언 부분##
myT = None    #myT 변수에 None 선언    #None: 아무것도 없음

##메인 코드 부분##
myT = turtle.Turtle()    #myT를 turtle 대신에 사용되도록 함(= import turtle as myT)
myT.shape("turtle")    #turtle 모양을 'turtle'

for i in range(0, 4) :    #0부터 3까지
    myT.forward(200)    #거북이가 앞으로 200 이동
    myT.right(90)    #거북이가 오른쪽으로 90 회전

myT.done()    #거북이 종료
