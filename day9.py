#클래스 정의하기
"""class Rabbit:
    #변수
    shape = ""
    xPos = 0
    yPos = 0
    #함수
    def goto(self,x,y):
        self.xpos = x
        self.ypos = y
"""
#클래스 사용
#객체이름 = 클래스(클래스는 클래스 이름으로 바로 사용할 수가 없음)
#반드시 클래스를 객체이름(변수)로 카피해서 사용한다
"""rabbit = Rabbit() #인스턴스 생성
#객체이름.변수
rabbit.shape = input()
a = rabbit.shape
#객체이름.함수
rabbit.goto(100,200)
print(a)
"""
"""
class Rabbit:
    #변수
    shape = ""
    xPos = 0
    yPos = 0
    #함수
    def goto(self,x,y):
        self.xPos = x
        self.yPos = y
        print(self.shape,"의 위치는",self.xPos, self.yPos,"입니다")

rabbit = Rabbit()
rabbit.shape = input()
x = input().split()
a = int(x[0])
b = int(x[1])
rabbit.goto(a,b)
"""
"""
class Rabbit:
    shape = ""
    xPos = 0
    yPos = 0
    def __init__(self): #객체 생성시 자동 실행(클래스 호출시 자동실행)
        self.shape = "토끼"
    def goto(self, x , y):
        self.xPos = x
        self.yPos = y
        print(self.shape,"의 위치는",self.xPos, self.yPos,"입니다")

rabbit = Rabbit()
x = input().split()
a = int(x[0])
b = int(x[1])
print("rabbit의 모양",rabbit.shape)
rabbit.goto(a,b)
"""


"""class Rabbit:
    shape = ""
    xPos = 0
    yPos = 0
    def __init__(self,value): #객체 생성시 자동 실행(클래스 호출시 자동실행)
        self.shape = value
    def goto(self, x , y):
        self.xPos = x
        self.yPos = y

rabbit2= Rabbit("원")
print(rabbit2.shape)"""
"""
class Rabbit:
    shape = ""
    xPos = 0
    yPos = 0
    def __del__(self):
        print(self.shape,self.xPos,self.yPos)
    def goto(self, x , y):
        self.xPos = x
        self.yPos = y

rabbit = Rabbit()
rabbit.shape = "토끼"
rabbit.goto(10,20)
del(rabbit)
"""
"""
class Rabbit:
    shape ="" 
    def __add__(self, other):
        print(self.shape,other.shape)


rabbit1 = Rabbit()
rabbit1.shape = "엽기토끼"
rabbit2 = Rabbit()
rabbit2.shape = "토끼"

rabbit1 + rabbit2"""


"""
class Rabbit:
    shape = ""
    xp = 0
    yp = 0

    def __init__(self):
        self.shape = "토끼"

    def __del__(self):
        pass

    def __add__(self, other):
        return self.xp + other.xp

    def goto(self, x, y):
        self.xp = x
        self.yp = y


rabbit1 = Rabbit()
rabbit2 = Rabbit()

rabbit1.xp = 10
rabbit1.yp = 10

rabbit2.xp = 20
rabbit2.yp = 20

print(rabbit1 + rabbit2)
"""

#고등학교 1학년 5개반이 있다.
#담당 국어 선생님: 홍길동
#각 반은 1-5,2-6,3-5,4-5,5-5명으로 구성됨
#각반 학생들의 국어 성적을 입력받아 총점과 평균을 구하는 코딩
#구현 조건 클래스를 이용한다.

# class line:
#     length = 0
#     def __init__(self,x):
#         self.length = x 
#         print("길이:",self.length)
#     def __add__(self,other):
#         return self.length + other.length
#     def __del__(self):
#         print("삭제",self.length)  
#     def __lt__(self,other):
#         return self.length < other.length
#     def __eq__(self,other):
#         return self.length == other.length
# x = input().split()
# ln1 = line(int(x[0]))
# ln2 = line(int(x[1]))
# print(ln1 + ln2)
# if ln1 < ln2:
#     print("ln2")
#     del(ln1)
# elif ln1 == ln2:
#     print("같다")
# else:
#     print("ln1")
#     del(ln2)

# class car:
#     color = ""
#     speed = 0
#     def __init__(self):
#         self.speed = 100
#     def upspeed(self,x):
#         self.speed += x
#         print(self.speed)

#     def downspeed(self,x):
#         self.speed -= x
#         print(self.speed)

# mycar1 = car() # 객체 생성
# print(mycar1.speed)
# mycar1.upspeed(30)
# mycar1.downspeed(60)

# class Rabbit:
#     shape =""
#     xpos = 0
#     ypos = 0
#     def goto(self,x,y):
#         self.xpos = x 
#         self.ypos = y
# class HouseRabbit(Rabbit):
#     owner = ""
#     def eatFeed(self):
#         print("집토끼가 모이를 먹습니다.")
# class MountainRabbit(Rabbit):
#     mountain ="" 
#     def eatWildgrass(self):
#         print("산토끼가 들풀을 먹습니다.")
# house = HouseRabbit()
# mountain = MountainRabbit()

# house.shape = "산토끼"
# print(house.shape)

# import turtle

# class seaTurtle(turtle.Turtle):
#     name = ' '
#     body = None
#     def __init__(self):
#         self.body = turtle.Turtle('triangle')
#         self.body.color("blue")
#         self.name = "바다거북"
#     def swim(self,x,y):
#         self.body.goto(x,y)
# class SandTurtle(turtle.Turtle):
#     name ='' 
#     body = None
#     def __init__(self):
#         self.body = turtle.Turtle('circle')
#         self.body.color("red")
#         self.name ="모래거북"
#     def walk(self,x ,y):
#         self.body.goto(x,y)

# seaTut, sandTut = None, None
# seaTut = seaTurtle()
# sandTut = SandTurtle()

# seaTut.swim(100,100)
# seaTut.body.write(seaTut.name, font=("Arial",20))

# sandTut.walk(-100,100)
# sandTut.body.write(sandTut.name, font=("Arial",20))
# goto color write 는 이미 있는 함수 <== Turtle 안에

import turtle 
import random

class Rabbit:
    myTurtle = None
    def __init__(self,myTut):
        self.myTurtle = myTut
        print("**토끼가 거북이 등에 올라탔습니다.**")
    def print_my_position(self):
        print("거북이 등 위의 토끼 위치는 현재",
              self.myTurtle.xcor(),",",self.myTurtle.ycor(),"입니다")
myTut, myReb = None, None
colorList = ["red","green","blue","magenta","orange","gray"]

turtle.setup(550,550)
turtle.screensize(500,500)

myTut = turtle.Turtle("turtle")
myRab = Rabbit(myTut) #객체 안에 다른 객체를 넣어서 연결함 포함관계
myTut.pensize(5)

for _ in range(20):
    x = random.randint(-250,250)
    y = random.randint(-250,250)
    color = random.choice(colorList)
    myTut.pencolor(color)
    myTut.goto(x,y)
    myRab.print_my_position( )
turtle.done( )
