"""
num1, num2, num3, num4 = 0, 0, 0, 0
hap = 0
num1 = int(input("수를 입력"))
num2 = int(input("수를 입력"))      
num3 = int(input("수를 입력"))
num4 = int(input("수를 입력"))  

hap = num1 + num2 + num3 + num4
print("합: %d" %hap)"""

#리스트 하나씩 사용하던 변수를 붙여서 한 줄로 붙여놓은 개념
#리스트는 여러개의 데이터를 하나의 변수로 묶어서 관리하는 자료구조
#각각의 데이터에는 번호(첨자)를 붙여서 접근함
#리스트는 변수의 일종으로 변수를 만드는 규칙과 동일하다
#리스트 이름 = [데이터1, 데이터2, 데이터3, ...]
#리스트는 대괄호[] 튜플은 괄호() 딕셔너리는 중괄호{}로 표현
#각 변수를 사용하는 경우 vs 리스트를 사용하는 경우
"""
num1, num2, num3, num4 = 0, 0, 0, 0
print(num1)  # 0 
numList = [1,2,3,4]
print(numList[0])  # 1
"""
"""
numList = [1,2,3,4] #기억장소가 4개 만들어졌다.
hap = 0
numList[0] = int(input("수를 입력"))
numList[1] = int(input("수를 입력"))
numList[2] = int(input("수를 입력"))
numList[3] = int(input("수를 입력"))

hap = numList[0] + numList[1] + numList[2] + numList[3]
print("합: %d" %hap)"""

#numlist = [] #빈 리스트를 만들어서 데이터를 입력받는 방법
#intlist = [10,20,30]
#strlist = ["안녕", "하이", "굿모닝"]
#데이터를 삭제하면서 방도 같이 삭제된다.
#데이터를 넣으면 늘어나고 빼면 줄어드는 특징이 있다.
#mixlist = [10,20,'난생'] #리스트는 데이터의 타입이 달라도 상관없다.

#리스트 이름. append(값) : 리스트의 맨 뒤에 값을 추가하는 함수
#리스트 이름. insert(위치, 값) : 리스트의 원하는 위치에 값을 추가하는 함수
#리스트 이름. remove(값) : 리스트에서 해당 값을 삭제하는 함수
#리스트 이름. pop(위치) : 리스트에서 해당 위치의 값을 삭제하는
#리스트 이름. clear() : 리스트의 모든 데이터를 삭제하는 함수
#리스트 이름. sort() : 리스트의 데이터를 오름차순으로 정렬하는 함수
#리스트 이름. reverse() : 리스트의 데이터를 내림차순으로 정렬하는
# 리스트 이름. index(값) : 리스트에서 해당 값의 위치를 반환하는 함수
# 리스트 이름. count(값) : 리스트에서 해당 값의 개수를 반환하는 함수
# 리스트 이름. len() : 리스트의 데이터 개수를 반환하는 함수
# 리스트 이름. sum() : 리스트의 데이터 합계를 반환하는 함수
# 리스트 이름. max() : 리스트의 데이터 중 최대값을 반환하는 함수
# 리스트 이름. min() : 리스트의 데이터 중 최소값을 반환하는 함수
# 리스트 이름. copy() : 리스트의 데이터를 복사하는 함수
# 리스트 이름. extend(리스트) : 리스트에 다른 리스트의 데이터를 추가하는 함수

#3사람의 시험점수를 입력받아 리스트에 저장하고 총점과 평균을 구하자
"""
dev = []
for x in range(3):
    num = int(input("수를 입력하시오"))
    if num == 0:
        break
    dev.append(num)
print(dev)
"""
"""dev = []
for x in range(3):
    dev.append(int(input("시험점수 입력:")))
tol = dev[0]+dev[1]+dev[2]
avg =(dev[0]+dev[1]+dev[2])/3
print("평균: %d 총점:%d" %(avg,tol))
"""
#번호가 범위를 벗어남 (방이 없는데 값을 집어 넣어서 에러가 뜸)
#위치를 특정하고 데이터를 집어넣어야 함 ex) testList = [0,0,0]
"""
testList = []
testList[0] = 100
testList[1] = 90
testList[2] = 80
print(testList)
"""

#append 는 맨 끝에서부터 "추가"하는거라서 방을 안만들어줘도 된다.
"""
testList = []
testList.append(100)
testList.append(90)
testList.append(80)
print(testList)
"""
"""
numList =["홍길동", 20,30]
for x in range(3):#(0,3,1) 2+1 이라서 표기는 3으로 함
    print(numList[x])# x 가 1씩 증가 하면서 3번 반복
"""

"""XList = [10,30]
XList.insert(1, 20)
print(XList[1])"""

"""numList = []
numList.append(10)
numList.append(20)
numList.append(30)
print(numList)"""

"""MIXList = []
MIXList.append("홍길동")
MIXList.append(20)
MIXList.append(175.4)
print(MIXList)"""

"""numList = [] 
for i in range(0,4):
    numList.append(0)
hap = 0
for i in range(0,4):
    numList[i] = int(input("숫자: "))
hap = numList[0] + numList[1] + numList[2] + numList[3]
print("합계: %d" %hap)"""

#첨자를 활용한 리스트 접근 방법
#첨자가 음수 값인 겨우 맨 뒤가 -1로 시작하여 그 바로 앞이 -2가 됨

"""numList = [10,20,30,40]
print("numList[-1]은",numList[-1],"numList[-2]는",numList[-2])#40 ,30
"""

#콜론":"을 사용하여 범위를 지정할 수 있다
"""
numList = [10,20,30,40]
print(numList[0:3])#0~2까지
print(numList[2:4])#2~3까지
"""
#콜론의 앞이나 뒤의 숫자를 생략할 수 있음
"""
print(numList[2:])#2~마지막 까지
print(numList[:2])#0이 생략되있음
"""
"""
numList = [10,20,30,40,50]
print(numList[2:4])
"""

#리스트의 덧셈
#요소들이 합쳐져 하나의 리스트가 됨

#리스트의 곱셈
#곱한 횟수만큼 리스트가 반복됨
"""
numList = [10, 20, 30]
myList = [40, 50, 60]
print(numList + myList)
print(numList *3)
"""
#인덱스의 범위를 벗어남(인덱스 오류)
"""numList = [10,20,30]
print(numList[3])#범위를 벗어남 2로 수정해야함
"""

#여러개의 명언을 리스트에 저장해 놓고, 저장된 명언을 랜덤하게 출력하는
#코드를 작성
"""
import random
deflist = ["가장 넉넉한 것은 만족할 줄 아는 것이다","행복은 성공의 열쇠이다",
           "아무리 작더라도, 강한 자를 이길 수 있다"]
print("오늘의 명언 ==> ",end = '')
ch = random.choice(deflist)
print(ch)
"""
"""
import random
deflist = ["가장 넉넉한 것은 만족할 줄 아는 것이다","행복은 성공의 열쇠이다",
           "아무리 작더라도, 강한 자를 이길 수 있다"]
today = random.randint(0 , len(deflist)-1)
"""
#저장되어 있는데이터 갯수를 len으로 세준다 데이커를 가르치킄 첨자는 0부터9
#따라서 1을 빼준다 
"""
print('오늘의 명언 ==>', deflist[today])
"""
#3사람의 국어 영어 수학 점수를 입력받아서 개인별 총점과 평균을 구합니다.
#단, 한꺼번에 입력을 받고
#출력을 한꺼번에 합니다.
#예 : 국어 영어 수학점수를 순서대로 입력하세요
# 100 100 90
# 90 90 100
# 90 90 100

# 출력 예 )
# 국어 영어 수학 총점 평균 
# =========================
# 100 100  90   XX   XX 
"""
sum1 , sum2, sum3 = 0 ,0 , 0
avg1 , avg2, avg3 = 0 ,0 , 0
hum1, hum2, hum3 = [] , [] , []
hum1 = input("이름과 국어 영어 수학 점수를 순서대로 입력하세요").split()
hum2 = input().split()
hum3 = input().split()

for x in range(1,4,1):
    hum1[x]= int(hum1[x])
    sum1 = sum1 + hum1[x] 
    hum2[x] = int(hum2[x])
    sum2 = sum2 + hum2[x]
    hum3[x]= int(hum3[x])
    sum3 = sum3 + hum3[x]
avg1 = sum1/(x)
avg2 = sum2/(x)    
avg3 = sum3/(x)
print("이름\t국어\t영어\t수학\t총점\t평균\n")
print("========================================================")
for x in range(4):
    print("%s\t"%hum1[x],end ='')
print("%d\t"%sum1,end = '')
print("%d\n"%avg1)
for x in range(4):
    print("%s\t"%hum2[x],end ='')
print("%d\t"%sum2,end = '')
print("%d\n"%avg2)
for x in range(4):
    print("%s\t"%hum3[x],end ='')
print("%d\t"%sum3,end = '')
print("%d\n"%avg3)
"""
#리스트 에 공간을 배정해서 만들기(방 3개를 미리 만들어둠)
"""
korList = [0,0,0]
engList = [0,0,0]
matList = [0,0,0]
totList = [0,0,0]
avgList = [0,0,0]

for i in range(0,3,1):
    korList[i] = int(input("국어성적:"))
    engList[i] = int(input("영어성적:"))
    matList[i] = int(input("수학성적:"))
    totList[i] = korList[i] + engList[i] + matList[i]
    avgList[i] = totList[i]/3
print("국어\t영어\t수학\t총점\t평균")
print("=================================================")
for i in range(3):
    print("%d\t %d\t %d\t %d\t %5.2f" %(korList[i],engList[i],matList[i],totList[i],avgList[i]))
"""
#방을 배정하지 않고 만들땐 append로 추가해서 만들어준다
"""
korList = []
engList = []
matList = []
totList = []
avgList = []

for i in range(0,3,1):
    korList.append(int(input("국어성적:")))
    engList.append(int(input("영어성적:")))
    matList.append(int(input("수학성적:")))
    totList.append(korList[i] + engList[i] + matList[i])
    avgList.append(totList[i]/3)
print("국어\t영어\t수학\t총점\t평균")
print("=================================================")
for i in range(3):
    print("%d\t %d\t %d\t %d\t %5.2f" %(korList[i],engList[i],matList[i],totList[i],avgList[i]))
"""

#리스트 값 변경하기 
"""
numList = [10,20,30]
numList[1:2] = [200,201]
print(numList)
"""

#리스트 안에 리스트 추가하기
"""numlist = [10,20,30]
numlist[1] = [200,201]
print(numlist)
"""

#append(값) : 맨 뒤에 값 추가하기
#insert(위치,값) : 정해진 위치에 값 삽입하기
"""numList = [10,20,30]
numList.insert(1,23)
print(numList)""" #[10,123,20,30] 123자리에 20을 넣어 값을 변경

#del( ):리스트의 항목삭제
numList = [10,20,30]
del(numList[1])#1번 자리의 데이터 삭제
print(numList)















