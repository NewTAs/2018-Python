## 변수 선언 부분 ##

a = int(input("시프트할 숫자는 :"))
i = int(input("출력할 횟수는 :"))

for i in range(1, i+1) :
    result = a << i
    print("%d << %d = %d" % (a, i, result))

for i in range(1, i+1) :
    result = a>>i
    print("%d >> %d = %d" % (a, i, result))
