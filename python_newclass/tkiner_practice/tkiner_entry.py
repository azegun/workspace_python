import tkinter
from math import *

window = tkinter.Tk()  # tkinter 클래스 선언해주고

# 윈도우 기본 설정
window.title("python UI")   # 윈도우 타이틀
window.geometry("640x400+650+380")    # 윈도우 사이즈랑, 위치(너비 x 높으 + x좌표 + y좌표)
window.resizable(False, False)    # 상하, 좌우 크기 조절 여부


def calc(event):        # event 매개변수가 들어가야지 작동
    label.config(text="결과="+str(eval(entry.get())))   # eval()함수는 식으로 들어온것을 계산해줌


entry = tkinter.Entry(window)
entry.bind("<Return>", calc)     # event 매개변수 생략가능, entry.bind가 함수 발생
entry.pack()


label = tkinter.Label(window)
label.pack()

window.mainloop()


# 예제
#
# window = tkinter.Tk()  # tkinter 클래스 선언해주고
#
# # 윈도우 기본 설정
# window.title("python UI")   # 윈도우 타이틀
# window.geometry("640x400+650+380")    # 윈도우 사이즈랑, 위치(너비 x 높으 + x좌표 + y좌표)
# window.resizable(False, False)    # 상하, 좌우 크기 조절 여부
#
#
# def calc():
#     sum1 = int(entry1.get())
#     sum2 = int(entry2.get())
#     str_convert = str(sum1+sum2)
#     label.config(text="결과="+str_convert)
#
#
# entry1 = tkinter.Entry(window)
# entry1.pack()
#
#
# entry2 = tkinter.Entry(window)
# entry2.pack()
#
# label = tkinter.Label(window, text="")
# label.pack()
#
# button = tkinter.Button(window, text="합계", command=calc)
# button.pack()
#
# window.mainloop()