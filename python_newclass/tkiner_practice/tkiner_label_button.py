import tkinter

window = tkinter.Tk()  # tkinter 클래스 선언해주고

# 윈도우 기본 설정
window.title("python UI")   # 윈도우 타이틀
window.geometry("640x400+650+380")    # 윈도우 사이즈랑, 위치(너비 x 높으 + x좌표 + y좌표)
window.resizable(False, False)    # 상하, 좌우 크기 조절 여부

count = 0


# 숫자 증가시키는 함수
def countUP():
    global count
    count += 1
    label.config(text=str(count))  # config 속성 바꾸는 메서드, text에 들어가려면 string으로 바꿔줘야함


# 라벨 설정
label = tkinter.Label(window,
                      state='disabled',
                      anchor="n",
                      text="0",
                      bitmap="info",
                      width=50,
                      height=50,
                      bg="white",
                      fg="red",
                      relief="solid")

label.pack()    # pack해줘야지 label 설정 입력

button = tkinter.Button(window,
                        text="OK",
                        overrelief="solid",
                        width=15,
                        command=countUP,         # 함수를 작동시킴.
                        takefocus=True,     # Tab키를 이용하여 이동여부
                        repeatdelay=1000,  # 버튼이 눌러진 상태에서 command 실행까지의 대기 시간
                        repeatinterval=100)    # 버튼이 눌러진 상태에서 command 실행의 반복 시간  (ms)
button.pack()


window.mainloop()  # ui 뛰우기