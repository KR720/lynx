PHL = ["C:/Users/Qertu/OneDrive/바탕 화면/컴퓨터 구조/디코더 (1) 0 일때.png",
       "C:/Users/Qertu/OneDrive/바탕 화면/컴퓨터 구조/디코더(2) 1일때.png",
       "C:/Users/Qertu/OneDrive/바탕 화면/컴퓨터 구조/멀티플렉서(1) 0일때.png",
       "C:/Users/Qertu/OneDrive/바탕 화면/컴퓨터 구조/멀티플렉서(2) 1일때.png",
        ]


from tkinter import*
from tkinter import messagebox

PHL = ["C:/Users/Qertu/OneDrive/바탕 화면/컴퓨터 구조/디코더 (1) 0 일때.png",
       "C:/Users/Qertu/OneDrive/바탕 화면/컴퓨터 구조/디코더(2) 1일때.png",
       "C:/Users/Qertu/OneDrive/바탕 화면/컴퓨터 구조/멀티플렉서(1) 0일때.png",
       "C:/Users/Qertu/OneDrive/바탕 화면/컴퓨터 구조/멀티플렉서(2) 1일때.png",
    ]
WB = Tk()
WB.geometry("800x800")
PH = PhotoImage(file = PHL[0])
LB = Label(WB, image= PH)
LB.image = PH
#출력 함수
def SHR(x):
    global PH
    match(x):
        case "봄":
            PH = PhotoImage(file = PHL[0])
            
        case "여름":
            PH = PhotoImage(file = PHL[1])
            
        case "가을":
            PH = PhotoImage(file = PHL[2])

        case "겨울":
            PH = PhotoImage(file = PHL[3])
        
    LB.config(image = PH)
    LB.image = PH #라벨 객체 안에 이미지 저장

BR1 = Button(WB, text = ("봄", 10) ,command = lambda:SHR("봄"))
BR2 = Button(WB, text = ("여름",10) ,command = lambda:SHR("여름"))
BR3 = Button(WB, text = ("가을",10) ,command = lambda:SHR("가을"))
BR4 = Button(WB, text = ("겨울",10) , command = lambda:SHR("겨울"))


BR1.place(x = 50, y= 10)
BR2.place(x = 100, y= 10)
BR3.place(x = 150, y=10)
BR4.place(x = 200, y=10)
LB.place(x=100, y=200)


WB.mainloop()