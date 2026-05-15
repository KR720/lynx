#만약에  num 이 100 보다 크면 들여쓰기 하는 문장이 3개
#따라서 들여쓰기가 되어 있지 않다면 if에 있는 조건문과 관계없이 출력된다.
"""
num = 200
if num > 100:
    print("100보다.")
    print("큽니다.")
    print("프로그램 끝.")
"""

#다음 단순if문은 오류가 발생한다. 그 이유는 무엇인가?
#if 문 내부에 들여쓰기가 되어있지 않다.
"""
number = 100
if number == 10:
print("10입니다")

print("프로그램 종료")
"""

#키보드로 국어 영어 수학 점수를 입력받아서 총점과 평균을 출력하고 평균값이
#60 이상이면 합격 그렇지 않으면 불합격
"""
kor = int(input("국어점수를 입력하시오"))
eng = int(input("영어점수를 입력하시오"))
math = int(input("수학점수를 입력하시오"))

avg = (kor+eng+math)/3

print("평균: %.2f",avg)

if avg >= 60 :
    print("합격")
else:
    print("불합격")
"""
"""
num = int(input("숫자를 입력 ==> "))
if num % 2 == 0:
    print("짝수 입니다.")
else:
    print("홀수 입니다.")
"""
#계속해서 반복
"""
while True :
    num = int(input("숫자를 입력 ==> "))
    if num == 0:
        break
    if num % 2 == 0:
        print("짝수 입니다.")
    else:
        print("홀수 입니다.")        
"""
#짝수 홀수를 찍는게 아니고 10번 반복했다고 가정했을때 짝수의 갯수와 홀수의
#갯수를 세어서 마지막에 출력한다
#for문
"""
count1, count2 = 0 , 0
for x in range (10):
    num = int(input("숫자를 입력 ==> "))
    if num%2 == 0:
        count1+=1
    else:
        count2+=1
print("홀수는 %d" %count2) 
print("짝수는 %d" %count1)         
"""
#while 문
"""
count1, count2, x = 0 , 0 , 0
while x < 10:
    num = int(input("숫자를 입력 ==> "))
    if num%2 == 0:
        count1 += 1
    else:
        count2 += 1
    x += 1
print("홀수는 %d" %count2)
print("짝수는 %d" %count1)
"""

#시험 과목이 첫번째 시험이 60점 이상 두번째 시험이 60점 이상이면 합격
#그렇지 않으면 불합격 (중첩 if 문) 
"""
T1 =  int(input("시험1 점수"))
T2 =  int(input("시험2 점수"))

if(T1 >= 60):
    if(T2 >= 60):
        print("합격")
    else:
        print("시험2 재시험")
else:
    print("시험1 재시험")
"""

#점수의 범위: 0 ~ 100
#점수가 0보다 작거나 100보다 큰수가 입력되면 입력오률를 출력한다
"""
score = int(input("점수를 입력 ==> "))
if(0 <= score <= 100):
    if score >= 90:
        print("A", end = '')
    elif score >= 80:
        print("B", end = '')
 f(0 <= score <= 100):
    if score >= 90:
        print("A", end = '')
    elif score >= 80:
        print("B", end = '')
    elif score >= 70:
        print("C", end = '')
    elif score >= 60:
        print("D", end = '')
    else:
        print("F", end = '')
    print("학점입니다.\n")
else:
    print("입력오류입니다.")
"""
"""
score = int(input("점수를 입력 ==> "))
if(score < 0 or score > 100):
     print("입력오류입니다.")
else:
    if score >= 90:
        print("A", end = '')
    elif score >= 80:
        print("B", end = '')
    elif score >= 70:
        print("C", end = '')
    elif score >= 60:
        print("D", end = '')
    else:
        print("F", end = '')
    print("학점입니다.\n")
"""
#random 을 이용해서 6개의 숫자를 생성한다.
#input 을 이용해서 6개의 숫자를 입력한다.(사용자가)
#컴퓨터가 생성한 6개의 수와 사용자가 입력한 6개의 수를 비교
#같은 수가 6개면 1등, 5개면 2등, 4개면 3등을 출력한다.
#로또 프로그램
"""
import random
count = 0
for i in range(6):
    num = int(input("번호 입력"))
    if(num == random.sample(range(1, 46), 6):
        count += 1
if(count == 6 ):
    print("1등")
elif( count == 5 ):
    print("2등")
elif( count == 4 ):
    print("3등")
else:
    print("꽝")
"""
#리스트 사용
"""
import random
LOList = []
NumList = []
count = 0
for i in range(6):
    LOList.append(random.randint(1,45))
for i in  range(6):
    NumList.append(int(input("번호를 입력하세여")))
for i in range(0,6,1):
    if LOList[0] == NumList[i]:
        count += 1
    if LOList[1] == NumList[i]:
        count += 1
    if LOList[2] == NumList[i]:
        count += 1
    if LOList[3] == NumList[i]:
        count += 1
    if LOList[4] == NumList[i]:
        count += 1
    if LOList[5] == NumList[i]:
        count += 1
if( count == 6 ):
    print("1등")
elif( count == 5 ):
    print("2등")
elif( count == 4 ):
    print("3등")
else:
    print("꽝")
    
print(LOList)
"""

"""
import random

# 컴퓨터 로또 번호 6개 생성 (중복 없이)
lotto = random.sample(range(1, 46), 6)

# 사용자 번호 6개 입력
user = []
for i in range(6):
    num = int(input("숫자 입력(1~45): "))
    user.append(num)

# 같은 숫자 개수 세기
count = 0
for x in user:
    if x in lotto:
        count += 1

# 결과 출력
print("컴퓨터 번호:", lotto)
print("사용자 번호:", user)

if count == 6:
    print("1등")
elif count == 5:
    print("2등")
elif count == 4:
    print("3등")
else:
    print("꽝")
"""
"""
import random
AI = random.choice(["가위","바위","보"])
roxH = input("가위바위보 입력")
if roxH == AI:
    print("DRAW")
elif AI == "보" and roxH == "가위":
    print("WIN")
elif AI == "바위" and roxH == "보":
    print("WIN")
elif AI == "가위" and roxH == "바위":
    print("WIN")
elif AI == "가위" and roxH == "보":
    print("lOSE")
elif AI == "바위" and roxH == "가위":
    print("lOSE")
elif AI == "보" and roxH == "바위":
    print("lOSE")
print("%s" %AI)
print("%s" %roxH)
"""
"""
import random
AI = random.choice(["가위","바위","보"])
roxH = input("가위바위보 입력")

if roxH == "가위":
    if AI == "가위":
        print("DRAW")
    elif AI == "바위":
        print("LOSE")
    else:
        print("WIN")
if roxH == "바위":
    if AI == "바위":
        print("DRAW")
    elif AI == "보":
        print("LOSE")
    else:
        print("WIN")
if roxH == "보":
    if AI == "보":
        print("DRAW")
    elif AI == "가위":
        print("LOSE")
    else:
        print("WIN")
print("%s" %AI)
print("%s" %roxH)
"""
"""
import turtle
import random

turtle.shape("turtle")
turtle.pensize(5)
turtle.pencolor("blue")

turtle.screensize(300,300)
turtle.setup(330,330)

while True:
    angle = random.randint(0, 360)
    distance = random.randint(10,100)
    turtle.right(angle)
    turtle.forward(distance)
    curX = turtle.xcor( )
    curY = turtle.ycor( )
    if (curX >= -150 and curX <= 150) and (curY >= -150 and curY <= 150) :
        print("GOOD BOY~")
else:
    turtle.goto( 0 , 0 )
    turtle.done( )
"""
"""
   elif score >= 70:
        print("C", end = '')
    elif score >= 60:
        print("D", end = '')
    else:
        print("F", end = '')
    print("학점입니다.\n")
else:
    print("입력오류입니다.")
"""
"""
score = int(input("점수를 입력 ==> "))
if(score < 0 or score > 100):
     print("입력오류입니다.")
else:
    if score >= 90:
        print("A", end = '')
    elif score >= 80:
        print("B", end = '')
    elif score >= 70:
        print("C", end = '')
    elif score >= 60:
        print("D", end = '')
    else:
        print("F", end = '')
    print("학점입니다.\n")
"""
#random 을 이용해서 6개의 숫자를 생성한다.
#input 을 이용해서 6개의 숫자를 입력한다.(사용자가)
#컴퓨터가 생성한 6개의 수와 사용자가 입력한 6개의 수를 비교
#같은 수가 6개면 1등, 5개면 2등, 4개면 3등을 출력한다.
#로또 프로그램
"""
import random
count = 0
for i in range(6):
    num = int(input("번호 입력"))
    if(num == random.sample(range(1, 46), 6):
        count += 1
if(count == 6 ):
    print("1등")
elif( count == 5 ):
    print("2등")
elif( count == 4 ):
    print("3등")
else:
    print("꽝")
"""
#리스트 사용
"""
import random
LOList = []
NumList = []
count = 0
for i in range(6):
    LOList.append(random.randint(1,45))
for i in  range(6):
    NumList.append(int(input("번호를 입력하세여")))
for i in range(0,6,1):
    if LOList[0] == NumList[i]:
        count += 1
    if LOList[1] == NumList[i]:
        count += 1
    if LOList[2] == NumList[i]:
        count += 1
    if LOList[3] == NumList[i]:
        count += 1
    if LOList[4] == NumList[i]:
        count += 1
    if LOList[5] == NumList[i]:
        count += 1
if( count == 6 ):
    print("1등")
elif( count == 5 ):
    print("2등")
elif( count == 4 ):
    print("3등")
else:
    print("꽝")
    
print(LOList)
"""

"""
import random

# 컴퓨터 로또 번호 6개 생성 (중복 없이)
lotto = random.sample(range(1, 46), 6)

# 사용자 번호 6개 입력
user = []
for i in range(6):
    num = int(input("숫자 입력(1~45): "))
    user.append(num)

# 같은 숫자 개수 세기
count = 0
for x in user:
    if x in lotto:
        count += 1

# 결과 출력
print("컴퓨터 번호:", lotto)
print("사용자 번호:", user)

if count == 6:
    print("1등")
elif count == 5:
    print("2등")
elif count == 4:
    print("3등")
else:
    print("꽝")
"""
"""
import random
AI = random.choice(["가위","바위","보"])
roxH = input("가위바위보 입력")
if roxH == AI:
    print("DRAW")
elif AI == "보" and roxH == "가위":
    print("WIN")
elif AI == "바위" and roxH == "보":
    print("WIN")
elif AI == "가위" and roxH == "바위":
    print("WIN")
elif AI == "가위" and roxH == "보":
    print("lOSE")
elif AI == "바위" and roxH == "가위":
    print("lOSE")
elif AI == "보" and roxH == "바위":
    print("lOSE")
print("%s" %AI)
print("%s" %roxH)
"""
"""
import random
AI = random.choice(["가위","바위","보"])
roxH = input("가위바위보 입력")

if roxH == "가위":
    if AI == "가위":
        print("DRAW")
    elif AI == "바위":
        print("LOSE")
    else:
        print("WIN")
if roxH == "바위":
    if AI == "바위":
        print("DRAW")
    elif AI == "보":
        print("LOSE")
    else:
        print("WIN")
if roxH == "보":
    if AI == "보":
        print("DRAW")
    elif AI == "가위":
        print("LOSE")
    else:
        print("WIN")
print("%s" %AI)
print("%s" %roxH)
"""
"""
import turtle
import random

turtle.shape("turtle")
turtle.pensize(5)
turtle.pencolor("blue")

turtle.screensize(300,300)
turtle.setup(330,330)

while True:
    angle = random.randint(0, 360)
    distance = random.randint(10,100)
    turtle.right(angle)
    turtle.forward(distance)
    curX = turtle.xcor( )
    curY = turtle.ycor( )
    if (curX >= -150 and curX <= 150) and (curY >= -150 and curY <= 150) :
        print("GOOD BOY~")
else:
    turtle.goto( 0 , 0 )
    turtle.done( )
"""
from tkinter import *
from tkinter import messagebox

PHL = [
    r"C:/Users/Qertu/OneDrive/바탕 화면/컴퓨터 구조/디코더 (1) 0 일때.png",
    r"C:/Users/Qertu/OneDrive/바탕 화면/컴퓨터 구조/디코더(2) 1일때.png",
    r"C:/Users/Qertu/OneDrive/바탕 화면/컴퓨터 구조/멀티플렉서(1) 0일때.png",
    r"C:/Users/Qertu/OneDrive/바탕 화면/컴퓨터 구조/멀티플렉서(2) 1일때.png"
]

WB = Tk()
WB.geometry("800x800")

PH = PhotoImage(file=PHL[0])
LB = Label(WB, image=PH)
LB.image = PH

def SHR(x):
    global PH

    match x:
        case "봄":
            PH = PhotoImage(file=PHL[0])

        case "여름":
            PH = PhotoImage(file=PHL[1])

        case "가을":
            PH = PhotoImage(file=PHL[2])

        case "겨울":
            PH = PhotoImage(file=PHL[3])

    LB.config(image=PH)
    LB.image = PH

BR1 = Button(WB, text="봄", command=lambda: SHR("봄"))
BR2 = Button(WB, text="여름", command=lambda: SHR("여름"))
BR3 = Button(WB, text="가을", command=lambda: SHR("가을"))
BR4 = Button(WB, text="겨울", command=lambda: SHR("겨울"))

BR1.place(x=50, y=10)
BR2.place(x=100, y=10)
BR3.place(x=150, y=10)
BR4.place(x=200, y=10)
LB.place(x=100, y=250)

WB.mainloop()


