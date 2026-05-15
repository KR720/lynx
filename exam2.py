DEV = ["4AJ4500","7BT3300","1AS2900","1AT3100","2BJ5000","3BS5000","1BT9000","2CS2300"]
MEM = {"A":"김진희","B":"임영웅","C":"아이유"}
CAR = {"J":"제네시스","T":"투산","S":"소나타"}

while True:
    print("="*100)
    print("1.입력\t2.입력순출력\t3.사원별 판매그래프\t4.총판매금액\t5.사원검색\t6.최우수사원\t7.검색")
    print("="*100)
    num = int(input("선택: "))
    if num == 1:
        testcase = int(input("입력할 횟수:"))
        for x in range(testcase):
            ADD_SCT = int(input("데이터 입력:"))
            DEV.append(ADD_SCT)
    if num == 2:
        dict ={}
        i = 1
        for x in DEV:
            dict[i] = x
            i += 1
            print("%d: %s"%(i,x))
    if num == 3:
        CSA =[]
        dic ={}
        for x in DEV:
            S = []
            S = list(x)
            CSA.append(S[1])
        Kim = CSA.count("A")
        Im = CSA.count("B")
        Ah = CSA.count("C")
        print("김진희 사원==>"+"*"*Kim+" ",Kim)
        print("임영웅 사원==>"+"*"*Im+" ",Im)
        print("아이유 사원==>"+"*"*Ah+" ",Ah)
    
    if num == 4:
        CI = []
        sum = 0
        for x in DEV:
            CI = list(x)
            PRI = CI[3]+CI[4]+CI[5]+CI[6]
            sum += int(PRI)
        print(sum)

    if num == 5:
        for x in DEV:
            CI = list(x)
            FRI = CI[1]
            if(FRI == "A"):
                print("찾았습니다 김진희\t%s"%x)
            elif(FRI == "B"):
                print("찾았습니다 임영웅\t%s"%x)
            elif(FRI =="C"):
                print("찾았습니다 아이유\t%s"%x)
            else:
                print("못찾았슴다")
    if num == 6:

        CI = []
        kim, im, ah = 0,0,0
        for x in DEV:
            CI = list(x)
            if(CI[1] =="A"):
                PRI = CI[3]+CI[4]+CI[5]+CI[6]
                kim += int(PRI)
                print(kim)
            elif(CI[1] == "B"):
                PRI = CI[3]+CI[4]+CI[5]+CI[6]
                im += int(PRI)
                print(im)
            elif(CI[1] == "C"):
                PRI = CI[3]+CI[4]+CI[5]+CI[6]
                ah += int(PRI)
                print(ah)
        if kim > ah:
            if kim > im:
                print("최우수 사원 김진희")
            else:
                print("최우수 사원 임영웅")
        elif kim < ah:
            if ah > im:
                print("최우수 사원 아이유")
            else:
                print("최우수 사원 임영웅")
    if num == 7:
        print("검색")
        num1 = 0
        CI = []
        print("번호 입력==> 1: 판매금액 2: 판매사원 3: 차종")
        num1 == int(input())
        a = int(input("검색할 번호:"))
        x = DEV[a]    
        CI = list(x)
        if num1 == 1:
            PRI = CI[3]+CI[4]+CI[5]+CI[6]
            print("판매금액은 %d입니다"%(int(PRI)))
        if num1 == 2:
            SCT = CI[2]
            if CI[2] =="A":
                print("김진희",x)
            elif CI[2] =="B":
                print("임영웅",x)
            elif CI[2] == "C":
                print("아이유",x)
            else: 
                print("입력오류")
        if num1 == 3:
            CAR_ = CI[3]
            if CAR_ == "J":
                print("제네시스",x)
            elif CAR_ == "T":
                print("투산",x)
            elif CAR_ =="S":
                print("소나타",x)
                            
# students = [
#     {"name": "kim", "kor": 80, "eng": 70, "math": 90},
#     {"name": "lee", "kor": 60, "eng": 85, "math": 75},
#     {"name": "park", "kor": 95, "eng": 90, "math": 100}
# ]

# dev ={}
# for x in students:
#     dev[x["name"]] = x["kor"] + x["eng"] + x["math"]
# while True: 
#     scl = int(input("번호 입력:"))
#     if scl == 1:
#         for x in dev:
#             print("%s의 총점은%d입니다" %(x,dev[x]))
#     elif scl == 2:
#         for x in dev:
#             print("%s의 평균은%d입니다" %(x,dev[x]/3))
#     elif scl == 3:
#         for x in dev:
#             if dev[x]/3 >= 80:
#                 print(x)


# books = [
#     {"title": "python", "price": 15000, "stock": 3},
#     {"title": "java", "price": 20000, "stock": 5},
#     {"title": "c", "price": 18000, "stock": 2}
# ]

# while True:
#     scl = int(input("번호 입력:"))
#     if scl == 1:
#         for x in books:
#             print("%s 가격:%d 재고:%d" %(x["title"],x["price"],x["stock"]))
#     if scl == 2:
#         sum = 0
#         for x in books:
#             al = x["price"]*x["stock"]
#             sum += al
#         print("총 재고 가치:%d" %sum)
#     if scl == 3:
#         for x in books:
#             if x["stock"] <= 3:
#                 print(x["title"])
#     if scl == 4:
#         print("재고 입력")
#         NA = input("책 이름 입력:")
#         for x in books:
#             if x["title"] == NA:
#                 found = 1

#                 if x["stock"] > 0:
#                     x["stock"] -= 1
#                     print("%s의 현재 재고 %d" % (x["title"], x["stock"]))
#                 else:
#                     print("품절")

#     if found == 0:
#         print("없는 책")
            
            

# menu = {
#     "coffee": {"price": 3000, "stock": 5},
#     "latte": {"price": 4000, "stock": 3},
#     "tea": {"price": 2500, "stock": 4}
# }
