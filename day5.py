#리스트에 점수 10개 미리 저장해놓고 평균을 구한뒤 평균 넘수 인원수

"""mlist = [10,20,30,40,50,60,70,80,90,100]
dev_sum, avg, cnt = 0,0,0
for x in mlist:
    dev_sum = dev_sum + x
avg = dev_sum/len(mlist)
for x in mlist:
    if( x > avg ):
        cnt = cnt + 1

print("인원수: %d 평균이상 사람수%d" %(len(mlist),cnt))
print("%d" %avg)
"""
#리스트로 아래처럼 출력한다.
"""mlist = [1,2,5,1,3]
for x in range(5):
    print("*"*mlist[x])
"""        
#두개의 값을 입력받아 두수의 범위의 수를 모두 더한다
"""num1 = int(input("insert number1"))
num2 = int(input("insert number2"))
dev = []
dev_sum = 0
dex = num1
for x in range(num1,num2,1):
    dev.append(dex)
    dev_sum = dev_sum + x
    dex = dex + 1
print("%d" %dev_sum)
"""
dev_phone = {"진수":"000","도현":"111","성재":"222","민서":"333"}

while True:
    print("="*40)
    print("0.종료\t1.출력\t2.추가\t3.검색\t4.삭제\n")
    print("="*40)
    insert = int(input("번호를 입력하세요"))
    if(insert == 1):
        for x in dev_phone.keys():
            print(x,"==> ", dev_phone[x])
    elif(insert == 2):#추가
        ADS = input("키 추가:")
        NDS = input("값 추가:")
        dev_phone[ADS] = NDS
        print(list(dev_phone))
        print(list(dev_phone.values()))
    elif(insert == 3):#검색
        find_out = input("검색:")
        if find_out in dev_phone.keys():
            print(dev_phone[find_out])
        else:
            print("NULL")
    elif(insert == 4):#삭제
        RED = input("삭제할 이름:")
        del(dev_phone[RED])
        print(list(dev_phone))
        print(list(dev_phone.values()))
    elif(insert == 0):
        break
    