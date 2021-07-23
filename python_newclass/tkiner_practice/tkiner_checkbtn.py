from tkinter import *
from tkinter import messagebox

window = Tk()  # tkinter 클래스 선언해주고

# 윈도우 기본 설정
window.title("python UI")   # 윈도우 타이틀
window.geometry("640x400+650+380")    # 윈도우 사이즈랑, 위치(너비 x 높으 + x좌표 + y좌표)
window.resizable(False, False)    # 상하, 좌우 크기 조절 여부


def show():
    print("item1: %d,\nitem2: %d\nitem3: %d\n" % (variable1.get(), variable2.get(), variable3.get()))
    messagebox.showinfo(
        "Button Clicked", "item1: {0},\nitem2: {1},\nitem3: {2}\n".format(
            variable1.get(), variable2.get(), variable3.get()))


def selectall():
    bt1.select()
    bt2.select()
    bt3.select()


def deselect():
    bt1.deselect()
    bt2.deselect()
    bt3.deselect()


variable1 = IntVar()
variable2 = IntVar()
variable3 = IntVar()

bt1 = Checkbutton(window, text="오늘도 힘내자1", variable=variable1)
bt2 = Checkbutton(window, text="오늘도 힘내자2", variable=variable2)
bt3 = Checkbutton(window, text="오늘도 힘내자3", variable=variable3)

bt1.pack()
bt2.pack()
bt3.pack()

buttonCheck = Button(window, text="check", width=40, overrelief="solid", command=show)
# button1.bind("<Double Button-1>", countPLus2)
buttonCheck.pack()

buttonSelectAll = Button(window, text="전체선택", width=40, overrelief="solid", command=selectall)
# button1.bind("<Double Button-1>", countPLus2)
buttonSelectAll.pack()

buttonDeSelectAll = Button(window, text="전체선택취소", width=40, overrelief="solid", command=deselect)
# button1.bind("<Double Button-1>", countPLus2)
buttonDeSelectAll.pack()

window.mainloop()
