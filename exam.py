votelist = [101,201,101,202,302,201,301,202,101,202]

while True:
    print("\t\t2024년 국회의원 선거관련 설문\n")
    print("="*100)
    print("=1.전체설문참여인원수\t2.입력\t3.출력\t4.연령대별인원수-그래프출력\t5.지지정당 - 개나리당/미나리당\n")
    print("="*100)
    num = int(input(" "))
    if num == 1:
        print("전체참여인원수:",end = '')
        print("%d명 입니다" %len(votelist))
    if num == 2:
        testcase = int(input("입력할 인원수:"))
        for x in range(testcase):
            print("번호를 입력하세요:",end ='')
            number = int(input())
            votelist.append(number)
    if num == 3:
        print("전체 출력")
        CLSI, CLSR = [], []
        cnt1, cnt2 = 0, 0
        for x in votelist:
            if x % 100 == 1:
                cnt1 += 1
                CLSI.append(x)
            if x % 100 == 2: 
                cnt2 += 1
                CLSR.append(x)
        more = 0
        if len(CLSI) > len(CLSR):
            more = len(CLSI)
            more = len(CLSR)
            for x in range(more-len(CLSR)):
                CLSI.append(0)
        else:
            more = len(CLSR)
            for x in range(more-len(CLSI)):
                CLSI.append(0)
        i,j=0,0
        for x in range(1,more+1):
            for i in range(i,x,1):
                print("%d" %CLSI[i],end =' ')
                i += 1
            for j in range(j,x,1):
                print("%d" %CLSR[j])
                j += 1
            print()
        print("기호 1번\t기호 2번")
    
    if num == 4: 
        print("연령대별인원수-그래프출력결과")
        c,cnt = 0, 0
        for x in votelist:
            dev = x // 100
            des = (x // 10)%10
            for j in range(10):
                if dev == j:
                    a = j * 10
                    c = a + des
                    print("%d는 %d 살 입니다"%(x,c))
        for x in votelist:
            dev = x // 100
            des = (x // 10)%10   
            for x in range(10):
                a = j * 10
                c = a + des
                dec = c // 10
                if dec == x:
                    print("%d대" %(x*10),end = ' ')
                    cnt += 1
                    print("*"*cnt,"%d명" %cnt)

                
    if num == 5:
        print("지지정당 출력")
        more = 0
        i,j = 0,0
        newlist1, newlist2 =[],[]
        for x in votelist:
            if x%100 == 1:
                newlist1.append(x)
            elif x%100 == 2:
                newlist2.append(x)
        if len(newlist1) > len(newlist2):
            more = len(newlist1)
            for x in range(more-len(newlist2)):
                newlist2.append(0)
        else:
            more = len(newlist2)
            for x in range(more-len(newlist1)):
                newlist1.append(0)
        for x in range(more):
            for i in range(i,x):
                print(newlist1[i],end = '                     ')
                i += 1
            for j in range(j,x):
                print(newlist2[j+1])
                j += 1
        print("기호 1번\t기호 2번")