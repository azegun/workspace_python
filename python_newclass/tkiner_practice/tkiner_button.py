import tkinter

window = tkinter.Tk()  # tkinter 클래스 선언해주고

# 윈도우 기본 설정
window.title("python UI")   # 윈도우 타이틀
window.geometry("640x400+650+380")    # 윈도우 사이즈랑, 위치(너비 x 높으 + x좌표 + y좌표)
window.resizable(False, False)    # 상하, 좌우 크기 조절 여부

photo = tkinter.PhotoImage(file="../logo-kakao.png")
count = 0
count2 = 0


def countPLus2(event):
    global count2
    count2 += 2
    label2.config(text=str(count2))


def countMinus2(event):     # bind()사용할 떄는 event 매개변수 입력해줘야함.
    global count2
    count2 -= 2
    label2.config(text=str(count2))


def countPlus():
    global count
    count += 1
    label.config(text=str(count))


def countMinus():
    global count
    count -= 1
    label.config(text=str(count))


label = tkinter.Label(window, text="0")
label.pack()

label2 = tkinter.Label(window, text="0")
label2.pack()

button1 = tkinter.Button(window, text="plus", width=40, overrelief="solid", command=countPlus, image=photo)
button1.bind("<Double Button-1>", countPLus2)
button1.pack()

button2 = tkinter.Button(window, text="minus", width=40,  overrelief="solid", command=countMinus)
button2.bind("<Double Button-1>", countMinus2)
button2.pack()


window.mainloop()
