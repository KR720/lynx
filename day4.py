"""
for i in range (0, 5, 2):
    print("%d회 %d을 대입한 후 print() 함수 수행"%((i+2)//2,i))
"""


    
"""
#리스트 0 ,1 ,2 로 어떤수가 들어가도 상관없음 앞에 "range" 빠짐
for i in [0, 1, 2]: 
    print("%d회 %d을 대입한 후 print() 함수 수행"%(i+1,i))
"""

"""
for i in range (0, 5, 2):
    print("%d회 %d을 대입한 후 print() 함수 수행"%((i/2)+1,i))
"""
"""
for i in range(1, 11, 1):
    print(i,end='')
"""
"""
std = int(input("학생수 입력"))
gob = 1
for x in range (1,std+1,1):
    gob = gob * x
    if(x == std):
        print("%d = %d" %(x,gob))
    else:
        print("%d*" %x,end = '')
print("경우의 수: %d\n" %(gob))
"""
"""
#ps
num = int(input("학생수:"))
gob = 1
for i in range(1,num+1,1):
    gob = gob * i
    if i<num :
        print("%d*" %i,end="")
    else :
        print("%d=%d" %(i,gob))
"""
"""
i = 0

for i in  range(1, 11, 1):
    hap = hap + i

print("1에서 10까지의 합:%d" %hap)"""

#10개의 수를  입력받아 짝수의 갯수와 홀수의 갯술르 세어 출력한다.
"""
div1, div2 = 0 ,0
for x in range (1 ,  10 , 1):
    num = int ( input("수를 입력"))
    if(num%2==0):
        div2 = div2 + 1
    elif(num%2 == 1):
        div1 = div1 + 1
print("홀수는 %d 짝수는 %d" %(div1, div2))
"""

"""
#초기값을 넣는 곳은 생략하면 안된다. 따라서 변수를 선언해줘야한다
even = 0
odd = 0
for i in range (10):
    num = int(input("숫자 입력"))
    if num%2 == 0 :
        even = even + 1
    else:
        odd = odd + 1
print("짝수  갯수: %d" %even)
print("짝수  갯수: %d" %odd)    
"""
"""
#점수를 입력받아 90점 이상 인원수 80점이상 인원수 70점 이상 인원 출력
ctd9, ctd8, ctd7 = 0, 0, 0
for x in range(10):
    std = int(input("점수 입력"))
    if(0<std<100):
        if(std >= 90):
            ctd9 = ctd9 + 1
        elif(std >= 80):
            ctd8 = ctd8 + 1
        elif(std >= 70):
            ctd8 = ctd7 + 1
print("90점 이상 %d 80점 이상 %d 70점 이상 %d" %(ctd9, ctd8, ctd7))
"""
"""
for x in range(1, 10 , 1):
    for k in range(1, 10, 1):
        mul = x * k
        print("구구단 %d * %d =%d "%(x , k, mul))
"""
"""
#ps
for i in range(2,10,1):
    print("\n%d단" %i)
    for j in range(1, 10 ,1):
        print("%d * %d = %d  " %(i, j , i*j),end = '')
"""
"""
for dan in range(1, 6):
    print(f"{dan}단", end="\t\t")
print()

for i in range(1, 10):
    for dan in range(1, 6):
        print(f"{dan} * {i} = {dan*i}", end="\t")
    print()
"""
"""
i = 0
while ( i < 3 ):
    print(i,": 난생처음 파이썬은 재미있습니다.")
    i = i + 1
"""
"""
for i in range(o , 3, 1):
    print(i,": 난생처음 파이썬은 재미있습니다.")
"""

#두개의 숫자와 연산기호(4칙연산) 입력받아
# +가 입력되면 합을 - 가 입력되면 차를 연산기호에 "STOP" 입력되면 멈춘다.
"""
dev, dev2 = 0 , 0
num1 = int(input("수를 입력"))
num2 = int(input("수를 입력"))
seq = input("기호 입력")
while True:
    if(seq == "-"):
        dev = num1 - num2 
    elif(seq == "+"):
        dev2 = num1 + num2
    elif(seq == "STOP"):
        break
    print("합: %d" %dev2)
    print("차: %d" %dev)
"""
"""
#4의 배수를 빼고서 합을 구하는 코딩
i, hap = 0, 0

for i in range(1, 101, 1):
    if i % 4 == 0:
        continue
    hap += i
print("!~100의 합계(4의 배수 제외):",hap)
"""

#4월 2일 까지 과제 
