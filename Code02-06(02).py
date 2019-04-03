import turtle as myT    #turtle함수를 불러오고 myT라는 이름을 사용

##함수 선언 부분##

##변수 선언 부분##

##메인 코드 부분##
myT.shape("classic")

for i in range(0, 4) :    #0부터 3까지
    myT.forward(200)    #거북이가 앞으로 200 이동
    myT.right(90)    #거북이가 오른쪽으로 90 회전

myT.done()    #거북이 종료
