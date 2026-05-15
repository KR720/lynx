

# for i in range (3):
#     di = ["A","B","C"]
#     name = di[i]
#     print(name,"님. 두 숫자를 입력하세요:")
#     num1 = int(input("정수1==>"))
#     num2 = int(input("정수2==>"))
#     hap = num1 + num2
#     print("결과 :",hap)

# def cal(k,x,y):
#     hap = 0
#     match(k):
#         case '+':
#             hap = x + y
#         case '-':
#             hap = x - y
#         case '/':
#             hap = x / y
#         case '%':
#             hap = x % y
#     print("결과값==>%.2f" %hap)
# apx = input("연산기호")
# num1 = float(input("첫번째 수 입력"))
# num2 = float(input("두번쨰 수 입력"))
# cal(apx,num1,num2)

#사칙연산 사용자 정의 함수 4개를 만든다
#메인코딩부분에 숫자 2개와 문자(+,-,..)을 입력받아
#출력도 메인코딩부분에서 한다

# def min(x,y):
#     return x - y
# def plus(x,y):
#     return x + y
# def mul(x,y):
#     return x * y
# def qur(x,y):
#     return x % y
# def cal(op,x,y):
#     match(op):
#         case "+":
#             return plus(x,y)
#         case "-":
#             return min(x,y)
#         case "*":
#             return mul(x,y)
#         case "%":
#             return qur(x,y)
# x = int(input("숫자1 :"))
# y = int(input("숫자2 :"))
# op = input("연산자(+,-,*,%):")
# print(cal(op,x,y))




#사각형 넓이
# class rec:
#     width = 0
#     length = 0
#     rec = 0
#     rec = width*length
#     def __init__(self):
#         self.width = 0
#         self.length = 0
#     def calc(self):
#         self.rec  = self.length * self.width
#         return self.rec
#     def __add__(self,other):
#         return self.rec + other.rec
#     def __del__(self):
#         print("instance deleted")

# nexus = rec()

# leng = float(input("가로길이:"))
# Leng = float(input("세로길이"))

# nexus.width = leng
# nexus.length =Leng

# qerr = nexus.calc()

# rex  = rec()

# lq = float(input("가로길이:"))
# ld = float(input("세로길이"))

# rex.width = lq
# rex.length = ld

# qer = rex.calc()

# shift = rex + nexus 

# print(shift)

# del(rex,nexus)


#서로다른 숫자 여섯개가 만들어지면 스탑



# import random
# x = 0
# led  = []
# def chc():
#     return random.randint(1,45)
# for x in range(1,7,1):
#     print(x,"번째 수 입력==>",end = '')
#     c = int(input())
#     led.append(c)
# load = []
# while len(load) < 6:
#     if chc() in load:
#         continue
#     else:
#         load.append(chc())

# def comp(x,y):
#     cnt = 0
#     for x in range:
#         for y in range:
#             if x == y:
#                 cnt += 1
#     return cnt

# match(comp(led, load)):
#     case 1:
#         print("꽝")
#     case 2:
#         print("꽝")
#     case 3:
#         print("꽝")
#     case 4:
#         print("3rd")
#     case 5:
#         print("2nd")
#     case 6:
#         print("1st")

# from datetime import datetime, timedelta 

# def getCurrent():
#     curdate = datetime.now()
#     return curdate

# def getafterdate(now, day):
#     retdate = now + timedelta(days=day)
#     return retdate

# now = getCurrent()

# day = int(input("며칠 뒤 날짜를 구할까요? : "))

# after = getafterdate(now, day)

# print("현재 날짜:", now.strftime("%Y-%m-%d %H:%M:%S"))
# print(day, "일 뒤 날짜:", after.strftime("%Y-%m-%d %H:%M:%S"))

# password = ""

# def checkpassword(pwd):

#     # 길이 검사
#     if len(pwd) < 8:
#         return False

#     # 영어 + 숫자만 있으면 실패
#     # 즉 특수문자가 최소 1개 필요
#     if pwd.isalnum():
#         return False

#     return True


# password = input("비밀번호 입력 : ")

# if checkpassword(password):
#     print("사용 가능한 비밀번호입니다.")
# else:
#     print("사용 불가능한 비밀번호입니다.")



# import turtle
# import random

# def getXYAS():
#     x, y, angle, size = 0, 0, 0, 0
#     x = random.randint(-250,250)
#     y = random.randint(-250,250)
#     size = random.randint(10, 50)
#     return x, y, size

# koreanStr ="""나랏말싸미 듕귁에 달아 문자와로 서로 사맛디 아니할쎄 
# 이런 젼차로 어린 백성이 니르고쳐 홀 배 이셔도
# 마참내 제 뜨들 시러펴디 몯 할 노미 하니라
# 내 이랄 위하야 어엿비 너겨 새로 스믈 여듧 짜랄 맹가노니 
# 사람마다 해여 수비 니겨 날로 쑤메 뼌한킈 하고져 할따라미니라
# """
# colorList = ["red","green","blue","black","magenta","orange"
#              ,"grey"]
# tX, tY, txtSize = 0,0,0

# turtle.shape('turtle')
# turtle.setup(550,550)
# turtle.screensize(500,500)
# turtle.penup( )
# turtle.speed(5)

# for ch in koreanStr:
#     tX, tY, txtSize = getXYAS()
#     color = random.choice(colorList)

#     turtle.goto(tX, tY)
#     turtle.pencolor(color)

#     turtle.write(ch, font=("맑은 고딕", txtSize, "bold"))

# turtle.done()


#주차관리 프로그램 
#시간에 따라서 요금계산
#디자인 설계 ==> 코딩 
#입력, 처리 , 출력 
#인터넷 참고 
#파이선 라이브러리로 계산하면 계산 안될 수 있음 

# 차량 번호판 인식 <== 차량 번호 입력 
# 할인 및 쿠폰 처리
# 주차 요금 정책 설정 <== 기본시간, 추가요금, 일일 최대요금
# 입차, 출차, 잔여 주차 확인
# 주차유도 시스템 
# 정기권 관리 <== 정기권 차량의 입출차 기록, 만료일 관리
# 통계 보고서 <== 일별, 월별 입출차 수, 주차 요금 수입, 주차
#회전율 통계 데이터 

#차량 번호판, 차량 출입사간, 차량 퇴장시간, 차량 부과 요금,
#부과 요금, 추가요금, 일일 최대요금, 입차, 출차, 잔여 주차 자리
#정기권 차량 관리
class DEV_CR:
    CR_SPC = []
    CR_inst = [] #차량번호:번호값, 출입시간:데이터,
                   #퇴장시간: 데이터,총 요금: 데이터
                   #시간 데이터 형식 "0000년 00월 00일 00시 00분"
                   #0~3:년 ,6~7:월, 10~11:일, 14~15:시, 18~19:분
    charge_per_min = 100
    charge_per_hour = 3000
    charge_per_day = 30000
    charge_per_month = 200000
    charge_per_year = 2000000
    discoun_per = 0
    def TM_SEC(slef,x):
       for i in x:
           TIME = 0
           QR, QR2 = 0, 0
           for k,j in i.items():
               if k == "Entrytime":
                   QR = j
               elif k == "Exitime":
                   QR2 = j
           YR_ST = int(QR[0:4])
           YR_EN = int(QR2[0:4])
           MN_ST = int(QR[6:8])
           MN_EN = int(QR2[6:8])
           DD_ST = int(QR[10:12])
           DD_EN = int(QR2[10:12])
           HR_ST = int(QR[14:16])
           HR_EN = int(QR2[14:16])
           MI_ST = int(QR[18:20])
           MI_EN = int(QR2[18:20])
           MN_DD = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30
                    ,7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
           START = (
               YR_ST * 365 * 24 * 3600 
               + sum(MN_DD[m] for m in range(1,MN_ST)) * 24 *3600
               + (DD_ST - 1) * 24 * 3600
               + HR_ST * 3600
               + MI_ST * 60
           )
           END = (
               YR_EN *365 * 24 * 3600
               + sum(MN_DD[m] for m in range(1,MN_EN)) * 24 * 3600
               + (DD_EN - 1) * 24 * 3600
               + HR_EN * 3600
               + MI_EN * 60
           )
           TIME = END - START
           i["total"] = TIME
    def charge(self,x):
         
        for i in x:
            PR_YN, PR_MN, PR_DD, PR_HR, PR_MI = 0, 0, 0, 0, 0
            if(i["total"]>=31536000):
                PR_YN = i["total"]//31536000 * self.charge_per_year
                i["charge"] = PR_YN
            elif(31536000>i["total"]>=2419200):
                PR_MN = i["total"]//2419200 * self.charge_per_month
                i["charge"] = PR_MN
            elif(2419200>i["total"]>=86400):
                PR_DD = i["total"]//86400 * self.charge_per_day
                i["charge"] = PR_DD
            elif(86400>i["total"]>=3600):
                PR_HR = i["total"]//3600 * self.charge_per_hour
                i["charge"] = PR_HR
            elif(3600>i["total"]>=60):
                PR_MI = i["total"]//60 * self.charge_per_min
                i["charge"] = PR_MI
            else:
                pass
    def __init__(self):
        self.CR_inst = [{"platenum":"",
                        "Entrytime":"",
                        "Exitime": "",
                        "total":0, 
                        "charge":0}]
        print("차량 데이터 초기화")
    def __del__(self):
        print("차량 데이터 삭제")
from tkinter import*

window = Tk()
DIS_CASE, DIS_ENT, DIS_EXT, TOTAL = "", "", "",0
import time
FAT = DEV_CR()
TESTCASE = int(input("총 출예정 차량 수:")) 
while True:
    PRC = [{"convin":20, "Entrytime":"", "Exitime":"","total":0,"charge":0},
           {"movie":30, "Entrytime":"", "Exitime":"","total":0,"charge":0}, 
           {"distore":20, "Entrytime":"", "Exitime":"", "total":0,"charge":0}]
    num = int(input("번호 선택"))
    match(num):
        case 1:
            for _ in range(TESTCASE): # 차량 번호 입력 밑 진입시간 
                DIS_CASE = str(input("차량번호 입력:"))
                DIS_ENT = time.strftime("%Y년 %m월 %d일 %H시 %M분")
                print("입차시간: ",DIS_ENT)
                FAT.CR_inst.append({"platenum":DIS_CASE,
                                    "Entrytime":DIS_ENT,
                                    "Exitime": DIS_EXT,
                                    "total":0, 
                                    "charge":0})
#차량 퇴장 시간 및 차량 시간 계산
        case 2:
            for x in FAT.CR_inst:
                if x["Entrytime"] == "":
                    continue
                else:
                    DIX_CASE = str(input("차량번호 입력"))
                    DIX_EXT = time.strftime("%Y년 %m월 %d일 %H시 %M분")
                    print("출차시간: ",DIX_EXT)
                    if x["platenum"] == DIX_CASE:
                        x["Exitime"] = DIX_EXT 
                    FAT.TM_SEC(FAT.CR_inst)
                    FAT.charge(FAT.CR_inst)#차량 요금 부과 
#차량 매장별 할인 쿠폰 별도 부과
        case 3:
            for x in FAT.CR_inst:
                CHR_ENT = time.strftime("%Y년 %m월 %d일 %H시 %M분")
                CHR = int(input("번호선택: 1:편의점 , 2:영화관, 3:면세"))
                for j in PRC:
                    match(CHR):
                        case 1:
                            CHR_EXT = time.strftime("%Y년 %m월 %d일 %H시 %M분")
                            if FAT.TM_SEC(PRC) < FAT.TM_SEC(x):
                                FAT.charge(PRC)  
                                x["charge"] -= PRC["charge"]*PRC["convin"]/100
                        case 2:
                            CHR_EXT = time.strftime("%Y년 %m월 %d일 %H시 %M분")
                            if FAT.TM_SEC(PRC) < FAT.TM_SEC(x):
                                FAT.charge(PRC)
                                x["charge"] -= PRC["charge"]*PRC["movie"]/100
                        case 3:
                            CHR_EXT = time.strftime("%Y년 %m월 %d일 %H시 %M분")
                            if FAT.TM_SEC(PRC) < FAT.TM_SEC(x):
                                FAT.charge(PRC)
                                x["charge"] -= PRC["charge"]*PRC["distore"]/100
    
#주차장 요금 변경
        case 4:
            pick = int(input("1. 주차장 요금 변경 2. 매장 할인률 변경"))
            match(pick):
                case 1:
                    slc = int(input("변경 요금 선택: 1.년 2.달 3.일 4. 시간 5. 분"))
                    match(slc):
                        case 1:
                            ch0 = int(input("금액 설정:"))
                            FAT.charge_per_year = ch0
                        case 2:
                            ch1 = int(input("금액 설정:"))
                            FAT.charge_per_month =ch1
                        case 3:
                            ch2 = int(input("금액 설정:"))
                            FAT.charge_per_day =ch2
                        case 4:
                            ch3 = int(input("금액 설정:"))
                            FAT.charge_per_hour = ch3
                        case 5:
                            ch4 = int(input("금액 설정:"))
                            FAT.charge_per_min = ch4
                case 2:
                     MR = int(input("1.편의점 2.영화관 3.면세"))
                     for x in PRC:
                        if MR == 1:
                            Ch0 = int(input("금액 설정"))
                            x["convin"] = Ch0
                        elif MR == 2:
                            Ch1 = int(input("금액 설정"))
                            x["movie"] = Ch1
                        elif MR == 3:
                            Ch2 = int(input("금액 설정"))
                            x["distore"] = Ch2 
#주차장 자리 설정

window.mainloop()
                    
