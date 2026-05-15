
"""print("주승환");
print("주승환");
print("주승환");"""


"""kor = 100
eng = 100
math = 50
hap = (kor + eng + math)/3
print(" hap=%.2f" %(hap))"""

"""str1 = "난생처음"
str2 = "파이선"
print(str1 , str2)
print(str1 + str2)"""

"""num1 = int(input("숫자 입력:"))
num2 = int(input("숫자 입력:"))
print("합 : ", num1+num2)
print("합 : %d" %(num1+num2))"""

#문제 국어 영어 수학점수를 입력받아 평균을 출력한다.

'''K = int(input())
E = int(input())
M = int(input())
Q = (K + E + M)/3
print("평균:%d " %(Q))'''

#사용자에게 이름과 전화번호를 입력받아 출력하는 프로그램

'''UN = input("이름 ==> ")
UP = input("전화번호 ==> ")
print("제 이름은",UN, "이고, 연락처는", UP,"입니다.")'''

#택배 정보를 입력받아 배송비와 함께 출력하는 프로그램

'''N = input("받는 사람: ")
AD = input("주소 : ")
W = int(input("무게 : "))
P = W*5
print("받는사람 ==>", N)
print("주소 ==>", AD)
print("무게 ==>", W)
print("배송비 ==> ",44 P,"원")
print("배송비 ==> %d 원" %P)
'''

#사용자가 키보드로 2개의 숫자를 입력하면 두 숫자의 덧셈, 뺄셈 , 곱셈
#나눗셈, 나머지 , 제곱을 계산하는 계산기를 만들어 봅시다.

"""num1 = int(input("숫자1 ==> " ))
num2 = int(input("숫자1 ==> " ))
print(num1, " - " , num2, "=", num1-num2)
print(num1, " + " , num2, "=", num1+num2)
print(num1, " * " , num2, "=", num1*num2)
print(num1, " / " , num2, "=", num1/num2)
print(num1, " % " , num2, "=", num1%num2)
print(num1, " ** " , num2, "=", num1**num2)
"""

#거북이 그래픽
'''import turtle'''#turtle기능을 포함함
'''turtle.shape('turtle')'''#윈도우 창이 나오면서 동시에 거북이 모양 결정함
#거북이를 앞으로 200만큼 이동시키기
'''turtle.forward(100)'''#100은 화면의 픽셀(점)의 개수를 의미함

'''turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
'''
'''for i in range(100):
    turtle.forward(10*i)
    turtle.left(i*10)'''
#입력된 숫자의 나머지 구하기
'''num1 = int(input("나눠지는 수 ==> " ))
num2 = int(input("나누는 수==> " ))
q = num1 // num2
r = num1 % num2
print(num1,"을(를)",num2,"(으)로 나눈 몫은", q,"입니다.")
print(num1,"을(를)",num2,"(으)로 나눈 나머지는", r,"입니다.")
'''
#문제 시간을 초단위로 입력받아 시, 분, 초로 출력한다.
#예)
#초단위로 입력하세요 : 3601
#출력 : 1시간 01분 1초
'''
T = int(input("초단위로 입력하세요: "))
Tq1 = T//3600
Tq2 = (T%3600)//60
Tq3 = T%60
print("출력: ",Tq1,"시간", Tq2,"분", Tq3,"초")
'''

wp = float(input("무게(파운드): "))

wkg = wp*0.453592

print("%f 파운드(1b)는 %f 킬로그램(kb)입니다." %(wp,wkg))

kg = float(input("무게(킬로그램): "))

wP = kg*2.204623

print("%f 킬로그램(kb)는 %f 파운드(1b)입니다." %(kg, wP))

