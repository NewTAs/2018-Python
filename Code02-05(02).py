import turtle    #turtle 함수를 불러온다.

##변수 선언 부분##
ques_1, ques_2, fo, rig, lef = [0] * 5    #ques_1, ques_2, fo, rig, lef 변수에 0을 대입한다.

##함수 선언 부분##
def t_fo_ri(a, b) :    #t_fo_ri 함수
    turtle.forward(a); turtle.right(b)    #거북이가 앞으로 a만큼 이동한 후, 오른쪽으로 b만큼 회전한다.

def t_fo_le(a, b) :    #t_fo_le 함수
    turtle.forward(a); turtle.left(b)      #거북이가 앞으로 a만큼 이동한 후, 왼쪽으로 b만큼 회전한다.

def t_ri_fo(a, b) :    #t_ri_fo 함수
    turtle.right(a); turtle.forward(b)    #거북이가 오른쪽으로 a만큼 회전한 후, 앞으로 b만큼 이동한다.

def t_le_fo(a, b) :    #t_le_fo 함수
    turtle.left(a); turtle.forward(b)     #거북이가 왼쪽으로 a만큼 회전한 후, 앞으로 b만큼 이동한다.

##메인 코드 부분##
turtle.shape("turtle")    #turtle 모양 - turtle

while True :    #반복문
    ques_1 = int(input("무엇을 먼저 하고 싶으신가요(1:회전 2:앞으로 이동) :"))     #출력
    if ques_1 == 1 :    #ques_1이 1일 때
        ques_2 = int(input("회전하고 싶은 방향을 입력해주세요(1:왼쪽 2:오른쪽) :"))    #출력
        if ques_2 == 1 :    #ques_2가 1일 때
            lef = int(input("왼쪽으로 얼마만큼 회전하고 싶으신가요? :")); fo = int(input("앞으로 가고싶은 거리를 입력해주세요. :"))    #출력

            t_le_fo(lef, fo)    #t_le_fo 함수를 사용하여, 거북이가 왼쪽으로 lef만큼 회전한 후, 앞으로 fo만큼 이동한다.
            
        elif ques_2 == 2 :    #ques_2가 2일 때
            rig = int(input("오른쪽으로 얼마만큼 회전하고 싶으신가요? :")); fo = int(input("앞으로 가고싶은 거리를 입력해주세요. :"))    #출력

            t_ri_fo(rig, fo)    #t_ri_fo 함수를 사용하여, 거북이가 오른쪽으로 rig만큼 회전한 후, 앞으로 fo만큼 이동한다.

        else :    #ques_2가 1과 2가 아닌 다른 것을 입력받았을 때
            print("숫자를 정확히 입력해주세요. 프로그램을 종료합니다.")    #출력
            break    #반복문 정지

    elif ques_1 == 2 :    #ques_1이 2일 때
        ques_2 = int(input("회전하고 싶은 뱡향을 입력해주세요(1:왼쪽 2:오른쪽)"))    #출력
        if ques_2 == 1 :    #ques_2가 1일 때
            lef = int(input("왼쪽으로 얼마만큼 회전하고 싶으신가요? :")); fo = int(input("앞으로 가고싶은 거리를 입력해주세요. :"))    #출력

            t_fo_le(fo, lef)    #t_fo_le 함수를 사용하여, 거북이가 앞으로 fo만큼 이동한 후, 왼쪽으로 lef만큼 회전한다.

        elif ques_2 == 2 :    #ques_2가 2일 때
            rig = int(input("오른쪽으로 얼마만큼 회전하고 싶으신가요? :")); fo = int(input("앞으로 가고싶은 거리를 입력해주세요. :"))    #출력

            t_fo_ri(fo, rig)    #t_fo_ri 함수를 사용하여, 거북이가 앞으로 fo만큼 이동한 후, 오른쪽으로 rig만큼 회전한다.

        else:    #ques_2가 1과 2가 아닌 다른 것을 입력받았을 때
            print("숫자를 정확히 입력해주세요. 프로그램을 종료합니다.")    #출력
            break    #반복문 종료

    else :    #ques_1이 1과 2가 아닌 다른 것을 입력받았을 때
        print("숫자를 정확히 입력해주세요. 프로그램을 종료합니다.")    #출력
        break    #반복문 종료
