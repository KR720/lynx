#Tkinter 에 있는 기능을 불러오는 코드
#Tk, Label, Button, Entry같은 GUI 도구 사용가능
#from tkinter import*
#GUI창을 만드는 코드
#TK()는 기본 윈도우 창 객체를 생성
#window = Tk()
#창이 바로 꺼지지 않고 계속 실행되게 만드는 코드
#GUI 창을 계속 띄워두고 사용자의 행동을 기다리는 역할
#window.mainloop()

#============================================
#from tkinter import*

#window = Tk()
#text 라벨에 표시할 글자
#label1 = Label(window, text ="ABC")
#맑은고딕 글꼴에 크기 24 굵게 bold로 표시
#fg는 foreground 로 글자색
#label2 = Label(window, text="CBS" , font = ("맑은고딕",24,"bold"),fg = "red")
#bg는 background 로 배경색
#width는 글자 20칸 정도의 너비
#height 라벨의 세로크기 설정
#anchor는 라벨안 어디에 붙일지 정함
#SE는 south east로 오른쪽 아래
#NW     N      NE
#W    CENTER    E
#SW     S      SE
#pack()은 만든 라벨을 실제 창에 배치
#label3 = Label(window, text ="NBC", bg= "orange",width = 20,height = 7, anchor = SE)
#label1.pack()
#label2.pack()
#label3.pack()
#window.mainloop()

#===========================================

#from tkinter import*

#window = Tk()

#이미지 파일을 불러옴
#PhotoImage는 tkinter에서 이미지를 사용가능
#r 은 raw string \같은 역슬래시 때문에 나는 오류
#photo = PhotoImage(file=r"C:\Users\Qertu\OneDrive\바탕 화면\컴퓨터 구조\멀티플렉서(2) 1일때.png")
#photo2 = PhotoImage(file=r"C:\Users\Qertu\OneDrive\바탕 화면\컴퓨터 구조\반가산기 구현 .png")

#이미지를 담는 라벨을 만드는 코드
#label1 = Label(window, image=photo)
#label2 = Label(window, image=photo2)
#label1을 창의 오른쪽에 배치함
#label1.pack(side = RIGHT)
#label2.pack(side = LEFT)
#window.mainloop()

#===========================================

#from tkinter import*

#window = Tk()
#window.title("계산기")
#window.geometry("400x500")
#Entry는 한 줄짜리 입력칸
#계산기에서 숫자나 계산식을 보여주는 화면 역할
#justrift = right은 입력된 글자를 오른쪽 정렬
#entry = Entry(window, font=("Arial",24),justify = "right")
#입력창을 화면에 배치하는 코드
#pack이 아니라 grid 사용 grid는 표처럼 나눠서 배치함
#row = 0은 0번째 줄에 배치
#column = 0은  0번째 칸부터 시작
#columnspan =4는 가로로 4칸을 차지하게함
#즉 입력창이 계산기 버튼 4개 너비만큼 길게 배치됨
#entry.grid(row = 0, column = 0, columnspan= 4)
#buttons = [
#    ["7","8","9","/"],
#    ["4","5","6","*"],
#    ["1","2","3","="],
#    ["0","c","=","+"]
#]
#x는 행 번호 역할 
#버튼이 4줄 4번 반복
#for x in range(4):
    #i 는 열 번호 역할
    #한 줄에 버튼 4개 만듦
#    for i in range(4):
#        btn = Button(
#            window,
#            text=buttons[x][i],
#            font = ("Arial",18),
#            width = 5,
#            height = 2
#        )
        #버튼을 화면에 배치시킴
        #x+1 은 0번째 줄에는 이미 입력창이 있어서
        #열번호 i 
        #padx, pady 는 좌우 여백, 위 아래 여백
#        btn.grid(row=x+1, column=i, padx=5,pady=5)
#window.mainloop()



from tkinter import*
from tkinter import messagebox
QS =  ["1.운동을 자주 한다", "2.아침을 먹는다","3.물을 충분히 마신다",
              "4.잠을 잘 잔다","5.스트레스가 적다"]
num = 0
#객체 생성
WD = Tk()
#창 크기
WD.geometry("400x300")
WD.config(bg = "orange")
#텍스트 박스 객체 생성
TB = Text(WD, width=25, height=5)
TB.pack(pady= 10)
#텍스트 출력
YC , NC = 0,0
def UPT():
    global YC, NC
    YC = 0
    NC = 0
    for x in REM:
        if x == 1:
            YC += 1
        elif x == 2:
            NC += 1
    TB.delete("1.0", END)
    TB.insert(END,"예:%d\n" %YC)
    TB.insert(END,"아니요:%d\n" %NC)
#이전
def next():
    global num 
    REM[num] = DEV.get()
    num += 1
    if num > 4:
        num = 0
    la.config(text = QS[num])
    DEV.set(REM[num])
    UPT()
#다음
def back():
    global num
    REM[num] = DEV.get()
    num -= 1
    if num < 0:
        num = 4
    la.config(text = QS[num])
    DEV.set(REM[num])
    UPT()
#설문 종료
def ED():
    REM[num] = DEV.get()
    UPT()
    result = messagebox.askyesno("종료","설문 종료할까요?")
    if result == True:
        WD.destroy() 

#라벨
la = Label(WD, text = QS[num],font= ("Futura", 25, "bold"), fg = "skyblue", bg="orange")
#버튼
BC = Button(WD, text = "<<이전", font = ("Arial",10,"bold"),fg = "gray", command = back,bg = "purple")
NX = Button(WD, text = "다음>>", font = ("Arial",10,"bold"),fg = "gray", command = next, bg ="purple")
FIN = Button(WD, text = "종료", font = ("Arial",10,"bold"),fg = "gray", command = ED, bg = "purple")
#라디오 버튼
DEV = IntVar()
REM = []
for x in range (0,len(QS)):
    REM.append(0)
#라디오 버튼은 벨류가 필요없다 1 또는 0이라서
yes = Radiobutton(WD, text = "예",variable = DEV, font = ("Futura",10,"bold"),fg = "green", value = 1, bg ="orange")
no = Radiobutton(WD, text = "아니요",variable = DEV, font = ("Futura",10,"bold"), fg = "red", value = 2, bg = "orange")
#붙여넣기
la.place(x=50, y=10)
yes.place(x=100, y=50, width=80, height=30)
no.place(x=200, y=50, width=80, height=30)
BC.place(x=50, y=120, width=80, height=30)
NX.place(x=250, y=120, width=80, height=30)
FIN.place(x=150, y=120, width=80, height=30)
NX.place(x = 250, y = 120, width = 80, height = 30)

WD.mainloop()