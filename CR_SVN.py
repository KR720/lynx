from datetime import datetime
#주차장 
class parking_lot:
#포함 데이터
    PRN = "주차 타워"
#전체 자리 수
    space = {   #space에는 차량 번호만 넣기
        "1F":{
            "A1":None,
            "A2":None,
            "A3":None,
            "B1":None,
            "B2":None,
            "B3":None
        },
        "2F":{
            "A1":None,
            "A2":None,
            "A3":None,
            "B1":None,
            "B2":None,
            "B3":None
        },
        "3F":{
            "A1":None,
            "A2":None,
            "A3":None,
            "B1":None,
            "B2":None,
            "B3":None
        }
    }
    #주차 중 차량 정보(차량 번호: 차량 상세 번호)
    parked_cars = {}
    #입차 기록
    ENT_RCS = []
    #출차 기록
    EXT_RCS = []
    #요금 정책
    EPL = {
        "분당 요금": 100,
        "시간당 요금":3000,
        "일일 요금":30000,
        "월별 요금":150000,
        "연간 요금":1500000,
        "무료 시간(분)":10
    }
    #할인 정책
    DCL = {
        "편의점":{
            "종류":"금액",
            "할인금액":500,
            "기준시간":0
        },
        "면세점":{
            "종류":"무료 이용 시간",
            "무료 시간(분)":120,
            "기준시간":0
        },
        "영화관":{
            "종류":"무료 이용 시간",
            "무료 시간(분)":100,
            "기준시간":0
        }
    }
    #차량번호: 정기권 번호
    SSS = {}
    #통계 데이터
    SCS = {
        "일별":{},
        "월별":{},
        "연별":{},
        "총 수입":0,
        "총 입차 수":0,
        "총 출차 수":0,
        "현재 차량 수":0
    }
    #빈 자리 확인
    def CR_remain(self,x): #주차장 자리
        FRC = {}
        for i,l in x.items():
            cs = []
            for q,w in l.items():
                if w == None:
                    cs.append(q)
            FRC[i] = cs
        CNT = 0 
        for a in FRC.values():
            CNT += len(a)
        print("총 빈자리는 %d자리 입니다" %CNT)    
        return CNT
    #만석 확인
    def CR_none(self,x): #주차장 자리
        FRC = {}
        for l in x.values():
            for w in l.values():
                if w == None:
                    print("만석이 아닙니다")
                    return False
        print("만석입니다")
        return True
    #입차 
    def CR_sp_in(self,x,y): #차량번호 ,이미지 
        if x in self.parked_cars:
            print("이미 입차한 차량입니다")
            return
        if self.CR_none(self.space):
            print("입차 불가")
            return 
        for i,l in self.space.items():
            for k,d in l.items():
                if d == None:
                    l[k] = x
                    now = datetime.now()
                    T_txt = now.strftime("%Y년 %m월 %d일 %H시 %M분")
                    print("입차 시간:",T_txt)
                    print(x,"차량이",i, k,"에 입차했습니다")
                    ERS = {
                        "차량번호":x,
                        "층":i,
                        "자리":k,
                        "입차시간":now,
                        "방문매장" :[],
                        "이미지경로":y,
                        "정기권":False
                    }
                    self.parked_cars[x] = ERS
                    self.ENT_RCS.append(ERS)
                    return now 
    #출차
    def CR_sp_out(self,x):#차량번호
        if x in self.parked_cars:
            now = datetime.now()
            T_txt = now.strftime("%Y년 %m월 %d일 %H시 %M분")
            print("출차 시간:",T_txt)
            ENT = self.parked_cars[x]["입차시간"]
            TIME = now - ENT
            print("주차시간:",TIME)
            MIN = TIME.total_seconds()/60
            TFM, TDM = self.DCI_DS(x)
            if self.CHR_ID(x) is False:
                D_MIN = MIN - TFM
                if D_MIN < 0:
                    D_MIN = 0
                CH = self.charge(D_MIN)
                FCH = CH - TDM
                if FCH < 0:
                    FCH = 0
            else:
                CH,FCH = 0,0
            print("할인 무료 시간:", TFM, "분")
            print("할인 금액:", TDM, "원")
            print("최종 요금:", FCH, "원")
            DRS = {
                "차량번호":x,
                "층": self.parked_cars[x]["층"],
                "자리": self.parked_cars[x]["자리"],
                "입차시간": ENT,
                "출차시간": now,
                "주차시간": TIME,
                "주차분": MIN,
                "할인무료시간":TFM,
                "할인금액":TDM,
                "기본요금":CH,
                "최종요금": FCH,
                "정기권":self.CHR_ID(x)
            }
            self.EXT_RCS.append(DRS)
            self.space[self.parked_cars[x]["층"]][self.parked_cars[x]["자리"]] = None 
            del self.parked_cars[x]
            print(x,"차량이 출차했습니다")
            return MIN
        else:
            print("입차 기록이 없습니다")
            return 
    #요금 계산
    def charge(self, x):  # x = 주차 시간(분)
        fmr = self.EPL["무료 시간(분)"]
        MI = int(x - fmr)
        if MI <= 0:
            print("무료")
            return 0
        charge = 0
        YN = MI // 15768000
        charge += YN * self.EPL["연간 요금"]
        MI %= 15768000
        MN = MI // 43200
        charge += MN * self.EPL["월별 요금"]
        MI %= 43200
        DD = MI // 1440
        charge += DD * self.EPL["일일 요금"]
        MI %= 1440
        HR = MI // 60
        charge += HR * self.EPL["시간당 요금"]
        MI %= 60
        charge += MI * self.EPL["분당 요금"]
        print("주차요금:",charge, "원")
        return charge
    #방문매장 등록
    def DCI(self,x,y,z): #차량번호, 매장명, 이용시간
        if x not in self.parked_cars:
            print("입차 기록이 없습니다")
            return
        if y not in self.DCL:
            print("등록되지 않은 매장입니다")
            return 
        self.parked_cars[x]["방문매장"].append({
            "매장명":y,
            "이용시간":z
        })
        print(x,"차량에",y,z,"분 방문 기록이 추가되었습니다")
    #할인 계산
    def DCI_DS(self,x):#차량번호 
        TFM = 0
        TDM = 0
        VI = self.parked_cars[x]["방문매장"]
        for x in VI:
            STN = x["매장명"]
            USR = x["이용시간"]
            PC = self.DCL[STN]
            if USR >= PC["기준시간"]:
                if PC["종류"] == "무료 이용 시간":
                    TFM += PC["무료 시간(분)"]
                elif PC["종류"] == "금액":
                    TDM += PC["할인금액"]
        return TFM,TDM
    #정기권
    def CAR_ID(self,x):#차량번호
        if x in self.SSS:
            print("이미 등록되었습니다.")
            return
        else:
            y = input("정기권 종류==>")
            ID_st = input("정기권 시작일 입력: (형식: xxxxx-xx-xx)")
            ID_ed = input("정기권 종료일 입력: (형식: xxxx-xx-xx)")
            START = datetime.strptime(ID_st,"%Y-%m-%d")
            END = datetime.strptime(ID_ed,"%Y-%m-%d")
            self.SSS[x] = {
                "종류":y,
                "시작일":START,
                "종료일":END,
                "상태":"등록"
            }
            print(x,"정기권이 등록되었습니다")
    #정기권 확인
    def CHR_ID(self,x):
        if x not in self.SSS:
            return False
        else:
            cmp_st = self.SSS[x]["시작일"]#시작일 종료일 모두 datetime 형식
            cmp_ed = self.SSS[x]["종료일"]#이여야 비교 가능
            now = datetime.now()
            if cmp_st <= now <= cmp_ed:
                self.SSS[x]["상태"] = "사용중"
                return True
            else:
                self.SSS[x]["상태"] = "만료"
                return False
    #통계 => 총 입차// 총 출차// 현재 차량 수// 총 수입
    def CR_DATA(self): #EXT_RCS (출차기록)
        self.SCS["총 출차 수"] = len(self.EXT_RCS)
        self.SCS["총 입차 수"] = len(self.ENT_RCS)
        self.SCS["현재 차량 수"]= len(self.parked_cars)
        revinew = 0 
        for x in self.EXT_RCS:            
            revinew += x["최종요금"]
        self.SCS["총 수입"] = revinew
    # 일별 통계
    def DRS_DD(self):
        self.SCS["일별"] = {}
        for x in self.ENT_RCS:
            day = x["입차시간"].date()
            if day not in self.SCS["일별"]:
                self.SCS["일별"][day] = {
                    "입차": 0,
                    "출차": 0,
                    "수입": 0
                }
            self.SCS["일별"][day]["입차"] += 1
        for x in self.EXT_RCS:
            day = x["출차시간"].date()
            if day not in self.SCS["일별"]:
                self.SCS["일별"][day] = {
                    "입차": 0,
                    "출차": 0,
                    "수입": 0
                }
            self.SCS["일별"][day]["출차"] += 1
            self.SCS["일별"][day]["수입"] += x["최종요금"]
        return self.SCS["일별"]
    #월별 통계
    def DRS_MN(self):
        self.SCS["월별"] = {}
        for x in self.ENT_RCS:
            day = x["입차시간"].strftime("%Y-%m")
            if day not in self.SCS["월별"]:
                self.SCS["월별"][day] = {
                    "입차": 0,
                    "출차": 0,
                    "수입": 0
                }
            self.SCS["월별"][day]["입차"] += 1
        for x in self.EXT_RCS:
            day = x["출차시간"].strftime("%Y-%m")
            if day not in self.SCS["월별"]:
                self.SCS["월별"][day] = {
                    "입차": 0,
                    "출차": 0,
                    "수입": 0
                }
            self.SCS["월별"][day]["출차"] += 1
            self.SCS["월별"][day]["수입"] += x["최종요금"]
        return self.SCS["월별"]
    #연별통계
    def DRS_YY(self):
        self.SCS["연별"] = {}
        for x in self.ENT_RCS:
            day = x["입차시간"].strftime("%Y")
            if day not in self.SCS["연별"]:
                self.SCS["연별"][day] = {
                    "입차": 0,
                    "출차": 0,
                    "수입": 0
                }
            self.SCS["연별"][day]["입차"] += 1
        for x in self.EXT_RCS:
            day = x["출차시간"].strftime("%Y")
            if day not in self.SCS["연별"]:
                self.SCS["연별"][day] = {
                    "입차": 0,
                    "출차": 0,
                    "수입": 0
                }
            self.SCS["연별"][day]["출차"] += 1
            self.SCS["연별"][day]["수입"] += x["최종요금"]
        return self.SCS["연별"]
    #검색기능
    def CR_search(self,x): #차량번호
        if x in self.parked_cars:
            car = self.parked_cars[x]
            print("=== 차량 검색 결과 ===")
            print("차량번호:",car["차량번호"])
            print("주차위치:",car["층"],car["자리"])
            print("입차시간:", car["입차시간"].strftime("%Y년 %m월 %d일 %H시 %M분"))
            print("방문매장:", car["방문매장"])
            print("정기권 여부:", self.CHR_ID(x))
            return car
        
        else:
            print("현재 주차 중인 차량이 아닙니다")
            return None
    #전체 주차 현황 
    def CRS(self):
        print("=== 전체 주차 현황 ===")
        for i, l in self.space.items():
            print("\n[%s]" %i)
            for x,y in l.items():
                if y == None:
                    print(x, ":빈자리")
                else:
                    print(x,":",y)                

    # 출차 기록 검색 
    def EXT_info(self, car_num):
        FIC = False

        for record in self.EXT_RCS:
            if record["차량번호"] == car_num:
                FIC = True
                print("=== 출차 기록 검색 결과 ===")
                print("차량번호:", record["차량번호"])
                print("주차위치:", record["층"], record["자리"])
                print("입차시간:", record["입차시간"])
                print("출차시간:", record["출차시간"])
                print("주차시간:", record["주차시간"])
                print("최종요금:", record["최종요금"])

        if FIC == False:
            print("출차 기록이 없습니다")

def SS(p):
    p.CR_DATA()

    print("=== 전체 통계 ===")
    print("총 입차 수:", p.SCS["총 입차 수"])
    print("총 출차 수:", p.SCS["총 출차 수"])
    print("현재 차량 수:", p.SCS["현재 차량 수"])
    print("총 수입:", p.SCS["총 수입"], "원")


def SDS(p):
    data = p.DRS_DD()

    print("=== 일별 통계 ===")
    for day, value in data.items():
        print(day, value)


def SMS(p):
    data = p.DRS_MN()

    print("=== 월별 통계 ===")
    for month, value in data.items():
        print(month, value)


def SYS(p):
    data = p.DRS_YY()

    print("=== 연별 통계 ===")
    for year, value in data.items():
        print(year, value)


def CM():
    p = parking_lot()

    while True:
        print()
        print("================================")
        print("        주차 관리 프로그램")
        print("================================")
        print("1. 입차")
        print("2. 출차")
        print("3. 현재 차량 검색")
        print("4. 출차 기록 검색")
        print("5. 전체 주차 현황")
        print("6. 빈자리 확인")
        print("7. 할인 등록")
        print("8. 정기권 등록")
        print("9. 전체 통계")
        print("10. 일별 통계")
        print("11. 월별 통계")
        print("12. 연별 통계")
        print("0. 종료")
        print("================================")

        dev = input("메뉴 선택: ")
        match dev:
            case "1":
                car = input("차량번호 입력: ")
                img = input("이미지 경로 입력: ")
                p.CR_sp_in(car, img)

            case "2":
                car = input("차량번호 입력: ")
                p.CR_sp_out(car)

            case "3":
                car = input("차량번호 입력: ")
                p.CR_search(car)

            case "4":
                car = input("차량번호 입력: ")
                p.EXT_info(car)

            case "5":
                p.CRS()

            case "6":
                p.CR_remain(p.space)
            case "7":
                car = input("차량번호 입력: ")
                store = input("방문매장 입력 ex) 편의점, 면세점, 영화관: ")
                try:
                    use_time = int(input("이용시간 입력(분): "))
                except ValueError:
                    print("이용시간은 숫자로 입력해야 합니다")
                    continue
                p.DCI(car, store, use_time)
            case "8":
                car = input("차량번호 입력: ")
                p.CAR_ID(car)
            case "9":
                SS(p)
            case "10":
                SDS(p)
            case "11":
                SMS(p)
            case "12":
                SYS(p)
            case "0":
                print("프로그램을 종료합니다.")
                break
            case _:
                print("잘못된 메뉴입니다. 다시 선택하세요.")
CM()