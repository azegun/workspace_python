from tkinter import *

window = Tk()  # tkinter 클래스 선언해주고

# 윈도우 기본 설정
window.title("python txt")   # 윈도우 타이틀
window.geometry("640x400+650+380")    # 윈도우 사이즈랑, 위치(너비 x 높으 + x좌표 + y좌표)
window.resizable(False, False)    # 상하, 좌우 크기 조절 여부

bx = 1
by = 2


def select1(event):
    value = "값 : " + str(scale1.get())
    label.config(text=value)
    bx = scale1.get()
    by = scale2.get()
    buttonRight.place(x=bx, y=by)


def select2(event):
    value = "값 : " + str(scale1.get())
    label.config(text=value)
    bx = scale1.get()
    by = scale2.get()       # 현재 위치에서 시작하기 위해 전역변수를 선언
    # by = scale2.get()
    buttonRight.place(x=bx, y=by)


var1 = IntVar()
var2 = IntVar()

scale1 = Scale(window, variable=var1,
               orient="vertical",
               showvalue=True,
               tickinterval=10,
               to=500, length=200,
               command=select1)
scale1.pack()

scale2 = Scale(window,
               variable=var2,
               orient="horizontal",
               showvalue=True, tickinterval=10,
               to=300, length=600,
               command=select2)
scale2.pack()

label = Label(window, text="0")
label.pack()

buttonRight = Button(window, text= "---------", overrelief="solid")
buttonRight.place(x=bx, y=by)


window.mainloop()