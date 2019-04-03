
##함수 선언 부분##
num_1, num_2, result_1, result_2, result_3 = [0] *5    #각 변수 선언

##메인 코드 부분##
num_1 = int(input("첫 번째 숫자를 입력해주세요. :"))    #첫 번째 숫자를 입력받는다.
num_2 =int(input("두 번째 숫자를 입력해주세요. :"))    #두 번째 숫자를 입력받는다.

result_1 = num_1 + num_2    #첫 번째 숫자와 두 번째 숫자를 더한 후, result_1에 선언
result_2 = num_1 * num_2    #첫 번째 숫자와 두 번째 숫자를 곱한 후, result_2에 선언
result_3 = pow(num_1, num_2)    #첫 번째 숫자를 밑수로, 두 번째 숫자를 지수로 한 후, 결과를 result_3에 선언

print(num_1, "+", num_2, "=", result_1)    #출력
print(num_1, "*", num_2, "=", result_2)    #출력
print(num_1, "^", num_2, "=", result_3)    #출력
