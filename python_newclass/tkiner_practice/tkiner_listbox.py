from tkinter import *
from math import *

window = Tk()  # tkinter 클래스 선언해주고

# 윈도우 기본 설정
window.title("python UI")   # 윈도우 타이틀
window.geometry("640x400+650+380")    # 윈도우 사이즈랑, 위치(너비 x 높으 + x좌표 + y좌표)
window.resizable(False, False)    # 상하, 좌우 크기 조절 여부


def delete_listbox():
    print(listbox.curselection())  # 튜플로 발생
    print(listbox.get(listbox.curselection()[0]))  # value 값 출력
    entry.insert(0, listbox.get(listbox.curselection()[0]))
    listbox.delete(listbox.curselection())


def entryTo_textbox(event):
    print("entry>> ", entry.get())
    txt.insert(END, entry.get())
    entry.delete(0, END)


listbox = Listbox(window, height=0, selectmode="extended")
listbox.insert(0, "1번")
listbox.insert(1, "2번")
listbox.insert(2, "3번")
listbox.insert(END, "4번")
listbox.insert(END, "5번")
listbox.pack()

entry = Entry(window)
entry.bind("<Return>", entryTo_textbox)     # event 매개변수 생략가능, entry.bind가 함수 발생

entry.pack()

txt = Text(window, width=50, height=20)
txt.pack()

button = Button(window, text="삭제", command=delete_listbox)
button.pack()

window.mainloop()

