from tkinter import *

window = Tk()  # tkinter 클래스 선언해주고

# 윈도우 기본 설정
window.title("python txt")   # 윈도우 타이틀
window.geometry("640x400+650+380")    # 윈도우 사이즈랑, 위치(너비 x 높으 + x좌표 + y좌표)
window.resizable(False, False)    # 상하, 좌우 크기 조절 여부

text = Text(window)
text.insert(INSERT, "Hello!!!")
text.insert(END, "..........")
text.pack()

text.tag_add("here", "1.0", "1.3")      # 인덱스로 지정 name 생성
text.tag_add("start", "1.06", "1.17")
text.tag_config("here", background="yellow", foreground="red")
text.tag_config("start", background="black", foreground="white")


window.mainloop()