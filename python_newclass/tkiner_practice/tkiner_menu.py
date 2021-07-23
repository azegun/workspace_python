from tkinter import *
from tkinter import messagebox

window = Tk()  # tkinter 클래스 선언해주고

# 윈도우 기본 설정
window.title("python UI")   # 윈도우 타이틀
window.geometry("640x400+650+380")    # 윈도우 사이즈랑, 위치(너비 x 높으 + x좌표 + y좌표)
window.resizable(False, False)    # 상하, 좌우 크기 조절 여부


def close():
    window.quit()           # 위젯 유지한채 mainloop() 이후 코드를 실행
    window.destroy()        # 위젯 제거한채 mainloop() 이후 코드를 실행


menubar = Menu(window)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="New File")
menu1.add_command(label="Open....")
menu1.add_separator()                           # 라인 잡아주는 역활
menu1.add_command(label="Exit", command=close)
menubar.add_cascade(label="File", menu=menu1)    # 위에 만든 command들을 추가 해주는 역활

menu2 = Menu(menubar, tearoff=True, selectcolor="red")   # tearoff 눈금자?
menu2.add_radiobutton(label="Undo", state="disable")
menu2.add_radiobutton(label="Redo")
menu2.add_radiobutton(label="Cut")
menubar.add_cascade(label="Edit", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_checkbutton(label="Python Shell")
menu3.add_checkbutton(label="Check Module")
menu3.add_checkbutton(label="Run Module")
menubar.add_cascade(label="Run", menu=menu3)

window.config(menu=menubar)                     # mainloop 키기 전에 메뉴들 다 입력시키고 config설정

menubutton = Menubutton(window, text="메뉴 메뉴버튼", relief="raised", direction="right")
menubutton.pack()

menu0 = Menu(menubutton, tearoff=0)
menu0.add_command(label="New File")
menu0.add_command(label="Open....")
menu0.add_separator()                           # 라인 잡아주는 역활
menu0.add_command(label="Exit", command=close)

menubutton["menu"] = menu0
window.mainloop()