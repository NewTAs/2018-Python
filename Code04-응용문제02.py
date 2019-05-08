import turtle    #turtle 프로그램을 가져오기

## 변수 선언 부분 ##

num, curX, curY = [0] * 3    #입력받을 숫자, 거북이의 X좌표, 거북이의 Y좌표
swidth, sheight = 1000, 300    #거북이 창 화면 크기

## 메인 코드 부분 ##
if __name__ == "__main__" :    #메인 코드 시작 부분
    turtle.title("거북이로 2진수 숫자 표현하기")    #거북이 프로그램 제목
    turtle.shape("turtle")    #거북이 모양
    turtle.setup(width = swidth+50, height = sheight+50)    #거북이가 이동할 수 있는 범위(1050, 350)
    turtle.screensize(swidth, sheight)    #거북이 창 화면 크기(1000, 300)
    turtle.penup()    #거북이 흔적없이 이동
    turtle.left(90)    #거북이가 90도 왼쪽으로 회전

    num = int(input("숫자를 입력헤주세요. :"))    #숫자를 입력 받는다.
    binary = bin(num)    #입력받은 정수를 2진수로 변환하여 binary라는 변수 이름으로 선언한다.
    curX = swidth / 2    #초기 위치 중 X좌표를 500으로 설정
    curY = 0    #초기 위치 중, Y좌표를 0으로 설정
    for i in range(len(binary) - 2) :    #변환한 2진수의 개수만큼 반복한다.
        #len은 길이를 나타냄. 2진수로 변환하면서 생기는 0b로 인하여 -2를 실행.
        turtle.goto(curX, curY)    #turtle이 (curX, curY) 좌표로 이동한다.
        if num & 1 :    #[비트 연산자] num의 2진수 맨 마지막 자리가 1일 때
            turtle.color("red")    #거북이의 색을 빨간색으로 바꿔준다.
            turtle.turtlesize(2)    #거북이의 크기를 2로 조정한다.

        else :    #[비트 연산자] num의 2진수 맨 마지막 자리가 1이 아닐 때
            turtle.color("blue")    #거북이의 색을 파란색으로 바꿔준다.
            turtle.turtlesize(1)    #거북이의 크기를 1로 조정한다.
        turtle.stamp()    #거북이의 자취마다 도장을 찍는다.
        curX -= 50     #curX = curX - 50 계산을 해준다.
        num >>= 1    #num의 2진수 비트를 오른쪽으로 하나의 숫자를 제거한다.

turtle.done()    #turtle 프로그램을 종료한다.
