#주차장 객체가 관리할 것
#현재 주차 중인 차량 목록
#입차 기록, 출차 기록
#요금 정책, 할인 정책
#정기권 차량 목록, 통계 데이터
#주차장 만석 여부, 빈 자리 안내
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
    def DCI_DS(self,x):
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
from tkinter import *
import sys
from datetime import datetime


# print()를 GUI 출력창으로 보내기
class TextRedirect:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, msg):
        self.text_widget.insert(END, msg)
        self.text_widget.see(END)

    def flush(self):
        pass


# 둥근 사각형 함수
def round_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [
        x1 + radius, y1,
        x2 - radius, y1,
        x2, y1,
        x2, y1 + radius,
        x2, y2 - radius,
        x2, y2,
        x2 - radius, y2,
        x1 + radius, y2,
        x1, y2,
        x1, y2 - radius,
        x1, y1 + radius,
        x1, y1
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)


# 보라색 그라데이션 배경
def draw_gradient(canvas, width, height, color1, color2):
    r1, g1, b1 = canvas.winfo_rgb(color1)
    r2, g2, b2 = canvas.winfo_rgb(color2)

    r_ratio = (r2 - r1) / height
    g_ratio = (g2 - g1) / height
    b_ratio = (b2 - b1) / height

    for i in range(height):
        nr = int(r1 + (r_ratio * i)) // 256
        ng = int(g1 + (g_ratio * i)) // 256
        nb = int(b1 + (b_ratio * i)) // 256
        color = f"#{nr:02x}{ng:02x}{nb:02x}"
        canvas.create_line(0, i, width, i, fill=color)


# 둥근 입력창
class RoundedEntry:
    def __init__(self, parent, label_text, placeholder, icon="⌕"):
        self.frame = Frame(parent, bg="#F7F6FF")

        self.label = Label(
            self.frame,
            text=label_text,
            bg="#F7F6FF",
            fg="#211A44",
            font=("Futura", 11, "bold"),
            anchor="w"
        )
        self.label.pack(anchor="w", padx=5, pady=(0, 5))

        self.canvas = Canvas(
            self.frame,
            width=310,
            height=48,
            bg="#F7F6FF",
            highlightthickness=0
        )
        self.canvas.pack()

        # 그림자
        round_rectangle(
            self.canvas,
            4, 5, 306, 47,
            radius=24,
            fill="#B8AEDB",
            outline=""
        )

        # 어두운 입력창
        round_rectangle(
            self.canvas,
            2, 2, 304, 44,
            radius=24,
            fill="#242037",
            outline="#3C345D",
            width=1
        )

        self.canvas.create_text(
            25,
            23,
            text=icon,
            fill="#A8A1C9",
            font=("Futura", 15)
        )

        self.entry = Entry(
            self.canvas,
            font=("Futura", 11),
            bg="#242037",
            fg="white",
            insertbackground="white",
            relief="flat",
            bd=0
        )
        self.entry.insert(0, placeholder)
        self.entry.config(fg="#9E98BD")

        self.entry.bind("<FocusIn>", self.clear_placeholder)
        self.entry.bind("<FocusOut>", self.add_placeholder)

        self.placeholder = placeholder
        self.canvas.create_window(60, 23, window=self.entry, width=220, height=25)

    def clear_placeholder(self, event):
        if self.entry.get() == self.placeholder:
            self.entry.delete(0, END)
            self.entry.config(fg="white")

    def add_placeholder(self, event):
        if self.entry.get() == "":
            self.entry.insert(0, self.placeholder)
            self.entry.config(fg="#9E98BD")

    def get(self):
        value = self.entry.get()
        if value == self.placeholder:
            return ""
        return value

    def pack(self, **kwargs):
        self.frame.pack(**kwargs)


# 둥근 버튼
class RoundedButton:
    def __init__(self, parent, text, command, icon="", width=145, height=48, main=True):
        self.command = command
        self.canvas = Canvas(
            parent,
            width=width,
            height=height,
            bg="#F7F6FF",
            highlightthickness=0,
            cursor="hand2"
        )

        if main:
            fill_color = "#6D37F5"
            shadow_color = "#B8A8FF"
            text_color = "white"
        else:
            fill_color = "#FFFFFF"
            shadow_color = "#D8D2F2"
            text_color = "#6D37F5"

        round_rectangle(
            self.canvas,
            4, 6, width - 4, height - 2,
            radius=18,
            fill=shadow_color,
            outline=""
        )

        round_rectangle(
            self.canvas,
            2, 2, width - 6, height - 6,
            radius=18,
            fill=fill_color,
            outline=""
        )

        self.canvas.create_text(
            width / 2,
            height / 2 - 2,
            text=f"{icon}  {text}",
            fill=text_color,
            font=("Futura", 12, "bold")
        )

        self.canvas.bind("<Button-1>", lambda event: self.command())

    def grid(self, **kwargs):
        self.canvas.grid(**kwargs)

    def pack(self, **kwargs):
        self.canvas.pack(**kwargs)


# 주차장 객체 생성
a = parking_lot()


# 윈도우 생성
window = Tk()
window.title("Parking Manager")
window.geometry("430x760")
window.resizable(False, False)

bg_canvas = Canvas(window, width=430, height=760, highlightthickness=0)
bg_canvas.pack(fill="both", expand=True)

draw_gradient(bg_canvas, 430, 760, "#7B3FF2", "#3A26D9")

# 배경 장식 원
bg_canvas.create_oval(-80, 80, 90, 250, fill="#8E5CFF", outline="")
bg_canvas.create_oval(330, -70, 510, 110, fill="#8E5CFF", outline="")
bg_canvas.create_oval(320, 610, 500, 790, fill="#5B45F0", outline="")

# 메인 카드 그림자
round_rectangle(
    bg_canvas,
    27, 35, 403, 735,
    radius=32,
    fill="#2C1B88",
    outline=""
)

# 메인 흰색 카드
round_rectangle(
    bg_canvas,
    22, 28, 398, 728,
    radius=32,
    fill="#F7F6FF",
    outline=""
)

main_frame = Frame(window, bg="#F7F6FF")
bg_canvas.create_window(210, 378, window=main_frame, width=355, height=690)


# 제목
Label(
    main_frame,
    text="Parking Manager",
    bg="#F7F6FF",
    fg="#211A44",
    font=("Futura", 24, "bold")
).pack(pady=(18, 18))


# 입력창
car_input = RoundedEntry(main_frame, "차량번호", "차량 번호 입력", "⌕")
car_input.pack(pady=(0, 8))

img_input = RoundedEntry(main_frame, "이미지 경로", "이미지 경로 입력", "▧")
img_input.pack(pady=(0, 8))

store_input = RoundedEntry(main_frame, "방문매장", "방문 매장 입력", "▣")
store_input.pack(pady=(0, 8))

time_input = RoundedEntry(main_frame, "이용시간 (분)", "이용 시간(분) 입력", "◷")
time_input.pack(pady=(0, 12))


# GUI 기능 함수
def gui_in():
    car = car_input.get()
    img = img_input.get()

    if car == "":
        print("차량번호를 입력하세요")
        return

    a.CR_sp_in(car, img)


def gui_out():
    car = car_input.get()

    if car == "":
        print("차량번호를 입력하세요")
        return

    a.CR_sp_out(car)


def gui_search():
    car = car_input.get()

    if car == "":
        print("차량번호를 입력하세요")
        return

    a.CR_search(car)


def gui_exit_search():
    car = car_input.get()

    if car == "":
        print("차량번호를 입력하세요")
        return

    a.EXT_info(car)


def gui_status():
    a.CRS()


def gui_discount():
    car = car_input.get()
    store = store_input.get()
    use_time = time_input.get()

    if car == "":
        print("차량번호를 입력하세요")
        return

    if store == "":
        print("방문매장을 입력하세요")
        return

    if use_time == "":
        print("이용시간을 입력하세요")
        return

    try:
        use_time = int(use_time)
    except ValueError:
        print("이용시간은 숫자로 입력하세요")
        return

    a.DCI(car, store, use_time)


def gui_statistics():
    a.CR_DATA()
    print("=== 전체 통계 ===")
    print("총 입차 수:", a.SCS["총 입차 수"])
    print("총 출차 수:", a.SCS["총 출차 수"])
    print("현재 차량 수:", a.SCS["현재 차량 수"])
    print("총 수입:", a.SCS["총 수입"], "원")


def clear_result():
    result.delete("1.0", END)


# 버튼 영역
button_frame = Frame(main_frame, bg="#F7F6FF")
button_frame.pack(pady=(0, 12))

RoundedButton(button_frame, "입차", gui_in, "▱", width=150).grid(row=0, column=0, padx=6, pady=5)
RoundedButton(button_frame, "출차", gui_out, "↪", width=150).grid(row=0, column=1, padx=6, pady=5)

RoundedButton(button_frame, "차량 검색", gui_search, "⌕", width=150).grid(row=1, column=0, padx=6, pady=5)
RoundedButton(button_frame, "출차 기록", gui_exit_search, "▤", width=150).grid(row=1, column=1, padx=6, pady=5)

RoundedButton(button_frame, "전체 현황", gui_status, "▦", width=150).grid(row=2, column=0, padx=6, pady=5)
RoundedButton(button_frame, "할인 등록", gui_discount, "◇", width=150).grid(row=2, column=1, padx=6, pady=5)

RoundedButton(main_frame, "전체 통계", gui_statistics, "▥", width=312, height=48).pack(pady=(0, 8))
RoundedButton(main_frame, "출력창 지우기", clear_result, "↻", width=312, height=44, main=False).pack(pady=(0, 12))


# 출력창 카드
result_canvas = Canvas(
    main_frame,
    width=312,
    height=125,
    bg="#F7F6FF",
    highlightthickness=0
)
result_canvas.pack()

round_rectangle(
    result_canvas,
    3, 5, 309, 123,
    radius=16,
    fill="#B8AEDB",
    outline=""
)

round_rectangle(
    result_canvas,
    1, 1, 307, 119,
    radius=16,
    fill="#18162C",
    outline=""
)

result = Text(
    result_canvas,
    width=34,
    height=5,
    font=("Futura", 10),
    bg="#18162C",
    fg="#BDB5FF",
    insertbackground="white",
    relief="flat",
    bd=0
)
result.insert(END, "출력 결과가 여기에 표시됩니다.\n기능을 실행하면 결과가 출력됩니다.\n")
result_canvas.create_window(154, 62, window=result, width=275, height=88)

sys.stdout = TextRedirect(result)


window.mainloop()


#할인 적용 요청
#통계 기록
#정기권 확인

#차량
#포함 데이터
#차량 번호
#입차 시간
#출차 시간
#주차 자리
#방문한 매장
#할인 쿠폰
#최종 요금

#차량 번호 저장
#입차 시간 저장
#출차 시간 저장
#주차 위치 저장
#방문 매장 정보 저장
#정기권 여부 저장

#주차 자리 (자리 상태 관리)

#포함 데이터
#자리번호
#비어 있는지 여부
#주차된 차량
#자리 위치 정보


#할인 정책(방문 매장에 따른 할인 계산)
#포함 데이터
#매장 이름
#매장별 할인 방식
#할인 금액
#무료 주차 시간

#정기권(정기권 차량인지 확인, 정기권 기간 확인, 정기권 차량은 요금 
#면제 또는 할인)
#포함데이터
#차량 번호
#정기권 시작일
#정기권 종료일
#정기권 종류
#예) 월 정기권 연 정기권 직원 정기권 VIP 정기권


#통계 보고서(주차장 이용 기록 분석)
#포함데이터
#일별 입차 수 
#일별 출차 수 
#월별 입차 수 
#월별 출차 수
#일별 수입
#월별 수입
#평균 주차 시간
#주차 회전율
#만석 횟수
#할인 적용 횟수
#정기권 이용 횟수
