from tkinter import *

window = Tk()  # tkinter 클래스 선언해주고

# 윈도우 기본 설정
window.title("python txt")   # 윈도우 타이틀
window.geometry("640x400+650+380")    # 윈도우 사이즈랑, 위치(너비 x 높으 + x좌표 + y좌표)
window.resizable(False, False)    # 상하, 좌우 크기 조절 여부


def btncmd(event):
    #  text와 엔트리의 내용 출력
    print("txt >>", txt.get("1.0", END), type(txt.get("1.0", END)))
    print("합 >> ", type(txt.get("1.0", END) + ent.get()))

    # print(txt.get("1.0", END) == "글자를 입력하시오")

    txt.insert(END, ent.get())
    ent.delete(0, END)


txt = Text(window, width=50, height=20)
txt.pack()

ent = Entry(window, width=50)
ent.bind("<Return>", btncmd)
ent.pack()

window.mainloop()