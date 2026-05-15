# from tkinter import*
# window = Tk()

# window.mainloop()
# 필수

#버튼 
#라벨 
#체크박스
#라디오박스

# from tkinter import*
# window = Tk()
# label1 = Label(window, text = "COOKBOOK~~ PYTHON을")
# label2 = Label(window, text = "열심히",font =("맑은고딕", 24, "bold"),fg = "blue")
# label3 = Label(window, text="공부 중입니다,",bg = "magenta",width = 20, height = 5, anchor = SE)

# label1.pack()
# label2.pack()
# label3.pack()

# window.mainloop()

# from tkinter import *

# window = Tk()

# photo = PhotoImage(file=r"C:\Users\Qertu\OneDrive\바탕 화면\컴퓨터 구조\멀티플렉서(2) 1일때.png")
# photo2 = PhotoImage(file=r"C:\Users\Qertu\OneDrive\바탕 화면\컴퓨터 구조\반가산기 구현 .png")

# label1 = Label(window, image=photo)
# label2 = Label(window, image=photo2)
# label1.pack(side=RIGHT)
# label2.pack(side=LEFT)

# window.mainloop()

# from tkinter import*
# window = Tk()
# window.title("계산기")
# window.geometry("300X300")
# entry = Entry(window, font=("Arial",24), justify="right")
# entry.grid(row = 0, column = 0, columnspan= 4)
# buttons = [
#     ["7","8","9","/"],
#     ["4","5","6","*"],
#     ["1","2","3","-"],
#     ["0","C","=","+"]
# ]
# for r in range(4):
#     for c in range(4):
#         Button(window, text= buttons[r][c])
# window.mainloop()

# from tkinter import *

# window = Tk()
# window.title("계산기")
# window.geometry("300x400")

# entry = Entry(window, font=("Arial", 24), justify="right")
# entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# buttons = [
#     ["7", "8", "9", "/"],
#     ["4", "5", "6", "*"],
#     ["1", "2", "3", "-"],
#     ["0", "C", "=", "+"]
# ]

# for r in range(4):
#     for c in range(4):
#         btn = Button(
#             window,
#             text=buttons[r][c],
#             font=("Arial", 18),
#             width=5,
#             height=2
#         )
#         btn.grid(row=r+1, column=c, padx=5, pady=5)

# window.mainloop()


# from tkinter import*
# window = Tk()

# button1 = Button(window, text = "파이썬 종료", fg = "red", command = quit)
# button1.pack()

# window.mainloop()

# from tkinter import*
# from tkinter import messagebox

# def myFunc():
#     messagebox.showinfo("close")

# window = Tk()
# photo = PhotoImage(file=r"C:\Users\Qertu\OneDrive\바탕 화면\컴퓨터 구조\반가산기 구현 .png")
# button1 = Button(window, image = photo, command = myFunc)

# button1.pack()
# window.mainloop()

#네이버
# import tkinter as tk
# from tkinter import messagebox


# class NaverStyleApp:
#     def __init__(self, root: tk.Tk):
#         self.root = root
#         self.root.title("네이버 느낌 메인 화면")
#         self.root.geometry("1200x800")
#         self.root.minsize(1000, 700)
#         self.root.configure(bg="#f5f6f7")

#         self.build_ui()

#     def build_ui(self):
#         self.build_top_bar()
#         self.build_search_area()
#         self.build_main_content()
#         self.build_footer()

#     def build_top_bar(self):
#         top_bar = tk.Frame(self.root, bg="#ffffff", height=50)
#         top_bar.pack(fill="x")
#         top_bar.pack_propagate(False)

#         left_menu = tk.Frame(top_bar, bg="#ffffff")
#         left_menu.pack(side="left", padx=20)

#         for text in ["메일", "카페", "블로그", "쇼핑", "뉴스", "지도"]:
#             btn = tk.Button(
#                 left_menu,
#                 text=text,
#                 bd=0,
#                 bg="#ffffff",
#                 activebackground="#ffffff",
#                 fg="#444444",
#                 font=("맑은 고딕", 10)
#             )
#             btn.pack(side="left", padx=8)

#         right_menu = tk.Frame(top_bar, bg="#ffffff")
#         right_menu.pack(side="right", padx=20)

#         for text in ["로그인", "회원가입", "알림"]:
#             btn = tk.Button(
#                 right_menu,
#                 text=text,
#                 bd=0,
#                 bg="#ffffff",
#                 activebackground="#ffffff",
#                 fg="#444444",
#                 font=("맑은 고딕", 10)
#             )
#             btn.pack(side="left", padx=8)

#     def build_search_area(self):
#         search_wrap = tk.Frame(self.root, bg="#f5f6f7", pady=25)
#         search_wrap.pack(fill="x")

#         logo = tk.Label(
#             search_wrap,
#             text="NAVER",
#             fg="#03c75a",
#             bg="#f5f6f7",
#             font=("Arial", 34, "bold")
#         )
#         logo.pack(pady=(10, 20))

#         search_box_outer = tk.Frame(
#             search_wrap,
#             bg="#03c75a",
#             padx=3,
#             pady=3
#         )
#         search_box_outer.pack()

#         search_box_inner = tk.Frame(search_box_outer, bg="#ffffff")
#         search_box_inner.pack()

#         self.search_entry = tk.Entry(
#             search_box_inner,
#             width=50,
#             font=("맑은 고딕", 17),
#             bd=0,
#             relief="flat"
#         )
#         self.search_entry.pack(side="left", padx=(12, 8), pady=12)
#         self.search_entry.bind("<Return>", self.search)

#         search_button = tk.Button(
#             search_box_inner,
#             text="검색",
#             command=self.search,
#             bg="#03c75a",
#             fg="white",
#             activebackground="#03c75a",
#             activeforeground="white",
#             font=("맑은 고딕", 12, "bold"),
#             width=8,
#             bd=0,
#             cursor="hand2"
#         )
#         search_button.pack(side="left", padx=8, pady=8)

#         keyword_frame = tk.Frame(search_wrap, bg="#f5f6f7")
#         keyword_frame.pack(pady=15)

#         for word in ["날씨", "증시", "웹툰", "쇼핑라이브", "게임", "부동산", "지도"]:
#             tag = tk.Label(
#                 keyword_frame,
#                 text=word,
#                 bg="#ffffff",
#                 fg="#555555",
#                 font=("맑은 고딕", 10),
#                 padx=10,
#                 pady=5,
#                 relief="solid",
#                 bd=1
#             )
#             tag.pack(side="left", padx=5)

#     def build_main_content(self):
#         content_wrap = tk.Frame(self.root, bg="#f5f6f7")
#         content_wrap.pack(fill="both", expand=True, padx=40, pady=10)

#         left_area = tk.Frame(content_wrap, bg="#f5f6f7")
#         left_area.pack(side="left", fill="both", expand=True)

#         right_area = tk.Frame(content_wrap, bg="#f5f6f7", width=280)
#         right_area.pack(side="right", fill="y", padx=(20, 0))
#         right_area.pack_propagate(False)

#         self.make_banner(left_area)
#         self.make_quick_icons(left_area)
#         self.make_news_section(left_area)
#         self.make_login_box(right_area)
#         self.make_trending_box(right_area)

#     def make_banner(self, parent):
#         banner = tk.Frame(parent, bg="#ffffff", height=140, bd=1, relief="solid")
#         banner.pack(fill="x", pady=(0, 15))
#         banner.pack_propagate(False)

#         title = tk.Label(
#             banner,
#             text="광고 / 배너 영역",
#             bg="#ffffff",
#             fg="#222222",
#             font=("맑은 고딕", 18, "bold")
#         )
#         title.pack(pady=(30, 5))

#         sub = tk.Label(
#             banner,
#             text="이 부분에 이벤트 배너나 공지 배너를 넣을 수 있음",
#             bg="#ffffff",
#             fg="#666666",
#             font=("맑은 고딕", 11)
#         )
#         sub.pack()

#     def make_quick_icons(self, parent):
#         quick = tk.Frame(parent, bg="#ffffff", bd=1, relief="solid")
#         quick.pack(fill="x", pady=(0, 15))

#         title = tk.Label(
#             quick,
#             text="자주 찾는 서비스",
#             bg="#ffffff",
#             fg="#222222",
#             font=("맑은 고딕", 13, "bold")
#         )
#         title.pack(anchor="w", padx=15, pady=(12, 5))

#         icons_frame = tk.Frame(quick, bg="#ffffff")
#         icons_frame.pack(fill="x", padx=10, pady=(0, 15))

#         services = [
#             "메일", "카페", "블로그", "쇼핑", "뉴스",
#             "증권", "부동산", "지도", "웹툰", "사전"
#         ]

#         for index, name in enumerate(services):
#             item = tk.Frame(icons_frame, bg="#f8f9fa", width=100, height=70, bd=1, relief="solid")
#             item.grid(row=index // 5, column=index % 5, padx=8, pady=8)
#             item.grid_propagate(False)

#             lbl = tk.Label(
#                 item,
#                 text=name,
#                 bg="#f8f9fa",
#                 fg="#333333",
#                 font=("맑은 고딕", 11)
#             )
#             lbl.place(relx=0.5, rely=0.5, anchor="center")

#     def make_news_section(self, parent):
#         news = tk.Frame(parent, bg="#ffffff", bd=1, relief="solid")
#         news.pack(fill="both", expand=True)

#         header = tk.Frame(news, bg="#ffffff")
#         header.pack(fill="x", padx=15, pady=(12, 5))

#         title = tk.Label(
#             header,
#             text="뉴스",
#             bg="#ffffff",
#             fg="#222222",
#             font=("맑은 고딕", 14, "bold")
#         )
#         title.pack(side="left")

#         more = tk.Button(
#             header,
#             text="더보기",
#             bd=0,
#             bg="#ffffff",
#             fg="#666666",
#             activebackground="#ffffff"
#         )
#         more.pack(side="right")

#         news_list = tk.Frame(news, bg="#ffffff")
#         news_list.pack(fill="both", expand=True, padx=15, pady=(0, 15))

#         sample_news = [
#             "오늘의 주요 뉴스 헤드라인이 여기에 표시됩니다.",
#             "파이썬 Tkinter로 포털 느낌 UI 만들기 예제 소개",
#             "언리얼 엔진 5 블루프린트 학습 가이드 정리",
#             "간단한 GUI 프로그램 디자인 팁 모음",
#             "검색창, 카드형 UI, 사이드바 만드는 방법"
#         ]

#         for text in sample_news:
#             row = tk.Frame(news_list, bg="#ffffff")
#             row.pack(fill="x", pady=6)

#             bullet = tk.Label(row, text="•", bg="#ffffff", fg="#03c75a", font=("맑은 고딕", 12, "bold"))
#             bullet.pack(side="left")

#             label = tk.Label(
#                 row,
#                 text=text,
#                 bg="#ffffff",
#                 fg="#333333",
#                 font=("맑은 고딕", 11),
#                 anchor="w"
#             )
#             label.pack(side="left", fill="x")

#     def make_login_box(self, parent):
#         login = tk.Frame(parent, bg="#ffffff", bd=1, relief="solid")
#         login.pack(fill="x", pady=(0, 15))

#         title = tk.Label(
#             login,
#             text="한 번에 로그인하고\n다양한 서비스를 이용하세요.",
#             bg="#ffffff",
#             fg="#333333",
#             justify="left",
#             font=("맑은 고딕", 11)
#         )
#         title.pack(anchor="w", padx=15, pady=(15, 12))

#         login_btn = tk.Button(
#             login,
#             text="NAVER 로그인",
#             bg="#03c75a",
#             fg="white",
#             activebackground="#02b350",
#             activeforeground="white",
#             font=("맑은 고딕", 12, "bold"),
#             bd=0,
#             height=2,
#             command=lambda: messagebox.showinfo("로그인", "로그인 기능은 예제입니다.")
#         )
#         login_btn.pack(fill="x", padx=15)

#         bottom = tk.Frame(login, bg="#ffffff")
#         bottom.pack(fill="x", padx=15, pady=12)

#         for text in ["아이디 찾기", "비밀번호 찾기", "회원가입"]:
#             btn = tk.Button(
#                 bottom,
#                 text=text,
#                 bd=0,
#                 bg="#ffffff",
#                 fg="#777777",
#                 activebackground="#ffffff",
#                 font=("맑은 고딕", 9)
#             )
#             btn.pack(side="left", padx=2)

#     def make_trending_box(self, parent):
#         trend = tk.Frame(parent, bg="#ffffff", bd=1, relief="solid")
#         trend.pack(fill="both", expand=True)

#         title = tk.Label(
#             trend,
#             text="실시간 관심 주제",
#             bg="#ffffff",
#             fg="#222222",
#             font=("맑은 고딕", 13, "bold")
#         )
#         title.pack(anchor="w", padx=15, pady=(12, 10))

#         topics = [
#             "1  파이썬 GUI",
#             "2  언리얼 5 블루프린트",
#             "3  점프맵 제작",
#             "4  Tkinter 디자인",
#             "5  게임 UI",
#             "6  검색창 만들기",
#             "7  Python 프로젝트",
#             "8  포트폴리오 제작",
#             "9  데스크톱 앱",
#             "10 웹 느낌 레이아웃"
#         ]

#         for item in topics:
#             lbl = tk.Label(
#                 trend,
#                 text=item,
#                 bg="#ffffff",
#                 fg="#333333",
#                 anchor="w",
#                 font=("맑은 고딕", 11)
#             )
#             lbl.pack(fill="x", padx=15, pady=4)

#     def build_footer(self):
#         footer = tk.Frame(self.root, bg="#ffffff", height=45)
#         footer.pack(fill="x", side="bottom")
#         footer.pack_propagate(False)

#         label = tk.Label(
#             footer,
#             text="ⓒ Tkinter Practice Page - 네이버 느낌의 학습용 예제",
#             bg="#ffffff",
#             fg="#777777",
#             font=("맑은 고딕", 9)
#         )
#         label.pack(pady=12)

#     def search(self, event=None):
#         keyword = self.search_entry.get().strip()
#         if not keyword:
#             messagebox.showwarning("검색", "검색어를 입력하세요.")
#             return
#         messagebox.showinfo("검색", f"'{keyword}' 검색 기능은 예제입니다.")


# if __name__ == "__main__":
#     root = tk.Tk()
#     app = NaverStyleApp(root)
#     root.mainloop()


# from tkinter import*
# from tkinter import messagebox
# window = Tk()

# def myFunc():
#     if chk.get()==0:
#         messagebox.showinfo("","체크버튼이 꺼졌어요")
#     else:
#         messagebox.showinfo("","체크버튼이 켜졌어요")

# chk = IntVar()#정수형 타입의 변수 생성 함수
# cb1 = Checkbutton(window, text="클릭하세요",variable =chk, command = myFunc)

# cb1.pack()
# window.mainloop()

# from tkinter import*
# window = Tk()

# def myFunc():
#     if var.get()==1:
#         label1.configure(text = "파이썬")
#     elif var.get()==2:
#         label1.configure(text = "C++")
#     else:
#         label1.configure(text = "Java")

# var = IntVar()
# rb1 = Radiobutton, text = "파이썬", variable = var, value = 1, command = myFunc
# rb1 = Radiobutton, text = "C++", variable = var, value = 2, command = myFunc
# rb1 = Radiobutton, text = "Java", variable = var, value = 3, command = myFunc


# from tkinter import*
# window = Tk()

# button1 = Button(window, text = "버튼1")
# button2 = Button(window, text ="버튼2")
# button3 = Button(window, text = "버튼3")

# button1.pack(side = LEFT)
# button2.pack(side = LEFT)
# button3.pack(side = LEFT)

# window.mainloop()

# from tkinter import*

# btnList = [None]*9
# fnameList =["C:/Users/Qertu/OneDrive/바탕 화면/컴퓨터 구조/디코더 (1) 0 일때.png","C:/Users/Qertu/OneDrive/바탕 화면/컴퓨터 구조/디코더 (1) 0 일때.png","C:/Users/Qertu/OneDrive/바탕 화면/컴퓨터 구조/디코더 (1) 0 일때.png",
#             "C:/Users/Qertu/OneDrive/바탕 화면/컴퓨터 구조/디코더 (1) 0 일때.png","C:/Users/Qertu/OneDrive/바탕 화면/컴퓨터 구조/디코더 (1) 0 일때.png","C:/Users/Qertu/OneDrive/바탕 화면/컴퓨터 구조/디코더 (1) 0 일때.png",
#             "C:/Users/Qertu/OneDrive/바탕 화면/컴퓨터 구조/디코더 (1) 0 일때.png","C:/Users/Qertu/OneDrive/바탕 화면/컴퓨터 구조/디코더 (1) 0 일때.png","C:/Users/Qertu/OneDrive/바탕 화면/컴퓨터 구조/디코더 (1) 0 일때.png"]
# photoList = [None]*9
# i,k = 0 ,0
# xPos, yPos = 0,0
# num = 0
# window = Tk()
# window.geometry("1500x1500")

# for i in range(0,9):
#     photoList[i] = PhotoImage(file = fnameList[i])
#     btnList[i] = Button(window, image = photoList[i])

# for i in range(0,3):
#     for k in range(0,3):
#         btnList[num].place(x = xPos, y= yPos)
#         num += 1
#         xPos += 70
#     xPos = 0
#     yPos += 70
# window.mainloop()

# from tkinter import*
# from time import*

# fnameList = ["C:/Users/Qertu/OneDrive/바탕 화면/컴퓨터 구조/디코더 (1) 0 일때.png","C:/Users/Qertu/OneDrive/바탕 화면/컴퓨터 구조/디코더(2) 1일때.png","C:/Users/Qertu/OneDrive/바탕 화면/컴퓨터 구조/멀티플렉서(1) 0일때.png",
#              "C:/Users/Qertu/OneDrive/바탕 화면/컴퓨터 구조/멀티플렉서(2) 1일때.png","C:/Users/Qertu/OneDrive/바탕 화면/컴퓨터 구조/반가산기 구현 .png"]
# photoList = [None]*5
# num = 0

# def clickNext():
#     global num
#     num += 1
#     if num > 4:
#         num =0
#     photo = PhotoImage(file = fnameList[num])
#     pLabel.configure(image = photo)
#     pLabel.image = photo

# def clickPrev():
#     global num
#     num -= 1
#     if num < 0:
#         num = 4
#     photo = PhotoImage(file = fnameList[num])
#     pLabel.configure(image = photo)
#     pLabel.image = photo


# window = Tk()
# window.geometry("700x500")
# window.title("사진 앨범 보기")

# btnPrev = Button(window, text = "<<이전", command = clickPrev)
# btnNext = Button(window, text ="다음 >>", command = clickNext)

# photo = PhotoImage(file = fnameList[0])
# pLabel = Label(window, image = photo)
# btnPrev.place(x= 250, y = 10)
# btnNext.place(x = 400, y = 10)
# pLabel.place(x = 15, y = 50)

# window.mainloop()


# from tkinter import*
# from tkinter import messagebox

# #설문문항
# questions = ["1. 운동을 자주 한다","2. 아침을 먹는다","3. 물을 충분히 마신다",
#              "4. 잠을 잘 잔다","5. 스트레스가 적다"]

# def clickNext():
#     global num
#     num += 1
#     if num > 4:
#         num = 0
# cnt, crs = 0, 0 
# window = Tk()
# btnNext = Button(window, text = "다음", command = clickNext)
# var = IntVar()
# rb1 = Radiobutton(window, text = "YES", variable = var, value = 1, command = cnt+=1) 
# rb2 = Radiobutton(window, text = "NO", variable = var, value = 2, command = crs += 1)

