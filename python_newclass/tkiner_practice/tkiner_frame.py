from tkinter import *

window = Tk()  # tkinter 클래스 선언해주고

# 윈도우 기본 설정
window.title("python txt")   # 윈도우 타이틀
window.geometry("640x400+650+380")    # 윈도우 사이즈랑, 위치(너비 x 높으 + x좌표 + y좌표)
window.resizable(False, False)    # 상하, 좌우 크기 조절 여부

frame1 = Frame(window, relief="solid", bd=2)
frame1.pack(side="left", fill="both", expand=True)

frame2 = Frame(window, relief="ridge", bd=2)
frame2.pack(side="right", fill="both", expand=True)

frame3 = Frame(window, relief="ridge", bd=2)
frame3.pack()

label1 = Label(frame1, text="hello")
label1.pack()

label2 = Label(frame2, text="world")
label2.pack()

label2 = Label(frame3, text="to")
label2.pack()

window.mainloop()