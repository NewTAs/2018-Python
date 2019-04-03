##변수 선언 부분##
sel, num = 0, 0    #sel과 num의 변수 선언

##메인 코드 부분##
sel = int(input("입력 진수를 결정해주세요(2/8/10/16) :"))    #숫자를 입력받는다
num = input("값 입력 :")    #문자를 입력받는다

if sel == 2 :    #sel이 2일 때
    num10 = int(num, 2)    #입력받은 문자를 2진수로 인식한 후, num10변수에 대입하여 선언

elif sel == 8 :    #sel이 8일 때
    num10 = int(num, 8)    #입력받은 문자를 8진수로 인식한 후, num10변수에 대입하여 선언

elif sel == 10 :    #sel이 10일 때
    num10 = int(num, 10)    #입력받은 문자를 10진수로 인식한 후, num10변수에 대입하여 선언

elif sel == 16 :    #sel이 16일 때
    num10= int(num, 16)    #입력받은 문자를 16진수로 인식한 후, num10변수에 대입하여 선언

print("2진수 ==> ", bin(num10))    #출력
print("8진수 ==> ", oct(num10))    #출력
print("10진수 ==> ", num10)    #출력
print("16진수 ==> ", hex(num10))    #출력
